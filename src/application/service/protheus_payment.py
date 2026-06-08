from odysseia.mixins import PagamentoDTO


class ProtheusPayment:

    @staticmethod
    def build(payment_data: PagamentoDTO | None) -> str:
        if not payment_data:
            return ""

        prazo = (
            "/".join(str(p) for p in sorted(payment_data.prazo))
            if payment_data.prazo
            else "7"
        )

        return (
            f"{payment_data.codigo}::"
            f"{payment_data.forma}::"
            f"{payment_data.metodo}::"
            f"{prazo}"
        )
