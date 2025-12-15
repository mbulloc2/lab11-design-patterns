from presidio_anonymizer.operators.operator import Operator
from presidio_anonymizer.operators import OperatorType


class Initial(Operator):
    def operate(self, text: str, params=None) -> str:
        parts = text.split()
        initials = []

        for part in parts:
            if part:
                initials.append(part[0].upper() + ".")

        return " ".join(initials)


    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

    def validate(self, params=None) -> None:
        # No params to validate for initial
        return
