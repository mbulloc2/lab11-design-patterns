from presidio_anonymizer.operators.operator import Operator
from presidio_anonymizer.operators import OperatorType


class Initial(Operator):
    def operate(self, text: str, params=None) -> str:
        result = []
        words = text.split()

        for word in words:
            prefix = ""
            initial = None

            for char in word:
                if char.isalnum():
                    initial = char.upper()
                    break
                else:
                    prefix += char

            if initial:
                result.append(f"{prefix}{initial}.")

        return " ".join(result)



    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

    def validate(self, params=None) -> None:
        # No params to validate for initial
        return
