import time

from app.logger import logger


def retry_operation(function, retries=3):

    for attempt in range(retries):

        try:

            result = function()

            logger.info(
                f"Operation successful on attempt {attempt + 1}"
            )

            return result

        except Exception as error:

            logger.error(
                f"Attempt {attempt + 1} failed: {error}"
            )

            if attempt < retries - 1:

                wait_time = 2 ** attempt

                logger.info(
                    f"Retrying after {wait_time} seconds"
                )

                time.sleep(wait_time)

    logger.warning(
        "All retry attempts failed. Using fallback."
    )

    return None
