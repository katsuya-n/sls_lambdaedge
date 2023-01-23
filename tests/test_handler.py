import handler
import json
import pytest

@pytest.mark.parametrize(
    "input_uri, expected_uri", [
    ("/hello.json", "/hello.json"),
    ("/not_found.json", "/not_found.json"),
    ("/dummy.json", "/not_found.json"),
])
def test_main(input_uri, expected_uri):
    event = {
        "Records": {
            0 : {
                "cf" : {
                    "request" : {
                        "uri" : input_uri
                    }
                }
            }
        }
    }

    expect = {
        "uri" : expected_uri
    }

    response = handler.main(event, "")
    assert response == expect
