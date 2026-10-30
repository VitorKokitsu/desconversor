from odysseia.mixins import PagamentoDTO


class ProtheusPayment:

    @staticmethod
    def build(payment_data: PagamentoDTO | None) -> str:
        if not payment_data:
            return ""

        if payment_data.forma is None and payment_data.metodo is None and payment_data.prazo is None:
            return payment_data.codigo or ""

        return str(payment_data)
