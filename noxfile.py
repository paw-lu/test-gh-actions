import json
import pprint

import nox
from nox import Session

PYTHON = "3.10"


@nox.session(python=PYTHON, tags=["build"])
def clone(session: Session) -> None:
    """Clone the repository and checkout latest release."""
    session.install("httpie")
    latest_release_api_data = session.run(
        "http",
        "https://api.github.com/repos/mwaskom/seaborn/releases/latest",
        "Accept:application/vnd.github+json",
        silent=True,
    )
    pprint.pprint(json.loads(latest_release_api_data))
