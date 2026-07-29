from app.pipeline import Pipeline


def test_pipeline_runs():

    document = (
        "Artificial Intelligence improves healthcare. "
        "Machine learning helps diagnosis. "
    ) * 20

    pipeline = Pipeline()

    result = pipeline.run(
        "healthcare",
        document
    )

    assert result["status"] == "success"

    assert len(result["summary"]) > 0