import sys
import json

from serializers.serializers import Serializer


class JsonSerializer(Serializer):
    def serialize(self, data: list) -> str:
        """Define serialization method"""

        try:
            return json.dumps(data, indent=4)

        except Exception as e:
            print(e.with_traceback, file=sys.stderr)
            raise SystemExit

    def deserialize(self, path: str) -> dict:
        """Define deserialization method"""

        try:
            with open(path, 'r') as json_file:
                return json.load(json_file)
                
        except Exception as e:
            print(e.with_traceback, file=sys.stderr)
            raise SystemExit