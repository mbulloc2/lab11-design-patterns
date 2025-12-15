from presidio_anonymizer.operators.operator import Operator
from presidio_anonymizer.operators import OperatorType


class Initial(Operator):
    def operate(self, text: str, params=None) -> str:
        return text

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

    def validate(self, params=None) -> None:
        # No params to validate for initial
        return
