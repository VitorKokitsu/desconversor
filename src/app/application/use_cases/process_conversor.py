from homero.enum import JobNameEnum
from odysseia.request.condpgto import CondicaoPagamentoRequestDTO
from odysseia.request.cotacao import CotacaoRequestDTO
from odysseia.request.retorno import RetornoFaturamentoRequestDTO

from app.application.mapper.condpgto import CondpgtoMapper
from app.application.mapper.cotacao import CotacaoMapper
from app.application.mapper.retorno import RetornoMapper
from app.application.services.job_identifier import JobIdentifier
from app.domain.ports.middleware_port import MiddlewareClientPort
from app.domain.ports.s3_port import S3Port


class ProcessConversorUseCase:

    def __init__(
        self,
        s3: S3Port,
        middleware_client: MiddlewareClientPort,
        process_identifier: JobIdentifier,
    ):
        self.s3 = s3
        self.middleware_client = middleware_client
        self.process_identifier = process_identifier

    def execute(self, s3_key: str, allow_send: bool) -> dict:
        raw_payload = self.s3.get_object(s3_key)

        job_name, raw_payload = self.process_identifier.identify(raw_payload)

        match job_name:
            case JobNameEnum.CONDICAO_PAGAMENTO:
                protheus_dto = CondicaoPagamentoRequestDTO(**raw_payload)
                middleware_dto = CondpgtoMapper.to_middleware(protheus_dto)
                if not allow_send:
                    return middleware_dto.model_dump()
                response = self.middleware_client.send_condpgto(middleware_dto)

            case JobNameEnum.COTACAO:
                protheus_dto = CotacaoRequestDTO(**raw_payload)
                middleware_dto = CotacaoMapper.to_middleware(protheus_dto)
                if not allow_send:
                    return middleware_dto.model_dump()
                response = self.middleware_client.send_cotacao(middleware_dto)

            case JobNameEnum.PEDIDO:
                print()

            case JobNameEnum.RETORNO_FATURAMENTO:
                protheus_dto = RetornoFaturamentoRequestDTO(**raw_payload)
                middleware_dto = RetornoMapper.to_middleware(protheus_dto)
                if not allow_send:
                    return middleware_dto.model_dump()
                response = self.middleware_client.send_retorno(middleware_dto)

            case _:
                raise ValueError("Processo não suportado")
