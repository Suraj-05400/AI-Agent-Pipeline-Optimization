import time

from app.agents import (
    ReaderAgent,
    CompressionAgent,
    RetrievalAgent,
    ValidationAgent
)

from app.logger import logger
from app.retry import retry_operation
from app.utils import estimate_tokens


class Pipeline:

    def __init__(self):
        self.reader = ReaderAgent()
        self.retriever = RetrievalAgent()
        self.compressor = CompressionAgent()
        self.validator = ValidationAgent()

    def run(self, query, document):

        start_time = time.time()

        logger.info("Pipeline execution started")

        print("=" * 50)
        print("Starting AI Pipeline")
        print("=" * 50)

        original_tokens = estimate_tokens(document)

        text = self.reader.execute(document)

        logger.info("Reader Agent completed")

        retrieved = retry_operation(
            lambda: self.retriever.execute(
                query,
                text
            )
        )

        if retrieved is None:
            logger.warning(
                "Retrieval failed. Using original context."
            )
            retrieved = text

        logger.info("Retrieval Agent completed")

        retrieved_tokens = estimate_tokens(retrieved)

        compressed = self.compressor.execute(
            retrieved
        )

        logger.info("Compression Agent completed")

        compressed_tokens = estimate_tokens(compressed)

        response = {
            "summary": compressed,
            "status": "success"
        }

        validated_response = self.validator.execute(
            response
        )

        print("\nTOKEN REPORT")
        print("----------------")

        print(
            "Original:",
            original_tokens
        )

        print(
            "Retrieved:",
            retrieved_tokens
        )

        print(
            "Compressed:",
            compressed_tokens
        )

        retrieval_saving = (
            (original_tokens - retrieved_tokens)
            / original_tokens
        ) * 100

        compression_saving = (
            (retrieved_tokens - compressed_tokens)
            / retrieved_tokens
        ) * 100

        print(
            f"\nRetrieval saved: {retrieval_saving:.2f}%"
        )

        print(
            f"Compression saved: {compression_saving:.2f}%"
        )

        execution_time = time.time() - start_time

        logger.info(
            f"Pipeline completed in {execution_time:.2f}s"
        )

        return validated_response.model_dump()
