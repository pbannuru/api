from typing import List
from app.internal.utils.timer import Timer
from app.services.opensearch_service import OpenSearchService
from app.dto.core_search_response_model import (
    SearchResponseMetadata,
    SearchResponseData,
    SearchResponse,
)
from app.sql_app.dbenums.core_enums import (
    PersonaEnum,
    DomainEnum,
    SourceEnum,
    LanguageEnum,
)


class CoreSearchService:

    def __init__(self, db=None):
        self.db = db

    async def search(
        self,
        query: str,
        domain: DomainEnum,
        device: str,
        persona: PersonaEnum,
        size: int,
        source: List[SourceEnum],
        language: LanguageEnum,
    ):

        timer = Timer().start_timer()
        response = OpenSearchService.get_search_response(
            query, domain, device, persona, size, source, language
        )
        timer.end_timer()

        # search_start_time_str = timer.strftime("%Y-%m-%d %H:%M:%S")
        OpenSearchService.log_search_response(
            query,
            domain,
            device,
            persona,
            source,
            language,
            timer.start_time_string,
            timer.elapsed_time_ms,
        )

        search_data_list = []
        for search_hits in response["hits"]["hits"]:
            if search_hits["_score"] >= 0.3:
                response_source = search_hits["_source"]
                response_source["score"] = search_hits["_score"]
                response_source["documentID"] = str(response_source["documentID"])
                search_data = SearchResponseData(**response_source)
                search_data_list.append(search_data)

        metadata_obj = SearchResponseMetadata(
            limit=size,
            size=len(search_data_list),
            query=query,
            device=device,
            persona=persona,
            domain=domain,
            source=source,
            language=language,
        )
        final_response = SearchResponse(metadata=metadata_obj, data=search_data_list)
        return final_response
