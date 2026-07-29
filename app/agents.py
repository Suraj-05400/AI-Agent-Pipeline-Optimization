from app.models import AgentResponse


class ReaderAgent:
    def execute(self, text):
        print(" Reading document...")
        return text


class CompressionAgent:
    def execute(self, text, max_words=100):

        print(" Compressing document...")

        words = text.split()

        compressed = " ".join(words[:max_words])

        return compressed


class RetrievalAgent:

    def execute(self, query, text):

        print(" Retrieving relevant information...")

        chunks = self.create_chunks(text)

        query_words = query.lower().split()

        scored_chunks = []

        for chunk in chunks:

            score = 0

            for word in query_words:
                if word in chunk.lower():
                    score += 1

            scored_chunks.append((score, chunk))

        # Highest score first
        scored_chunks.sort(reverse=True)

        unique_chunks = []

        for score, chunk in scored_chunks:

            if score > 0 and chunk not in unique_chunks:

                unique_chunks.append(chunk)

        return "\n".join(unique_chunks[:3])

    def create_chunks(self, text, size=50):

        words = text.split()

        chunks = []

        for i in range(0, len(words), size):

            chunk = " ".join(
                words[i:i + size]
            )

            chunks.append(chunk)

        return chunks


class ValidationAgent:

    def execute(self, response):

        print(" Validating response...")

        try:

            validated = AgentResponse(**response)

            return validated

        except Exception as error:

            raise Exception(
                f"Validation failed: {error}"
            )
