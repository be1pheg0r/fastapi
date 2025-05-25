from fastapi import APIRouter
from fastapi.src.utilities.llm_module.src.markup_to_x6 import x6_layout
from fastapi.src.utilities.llm_module.graphs import GenerationGraph
from fastapi.src.utilities.llm_module.states import generation
from fastapi.src.models.schemas.graphs_output import GenerationInput, GenerationOutput

router = APIRouter(prefix="/user_input", tags=["user_input"])



# только для MVP, потом заменить на бд
STATE = None
MODE = "api"

def generate_output(input_data: str, mode: str, local_model_cfg=None) -> GenerationOutput:
    """
    :param input_data: Входные параметры для генерации диаграммы
    :param process_query: Базовый промпт работы модели
    :return: BPMN диаграмма и дополнительная информация о процессе
    """
    global STATE
    if not STATE:
        STATE = generation(input_data)
    else:
        STATE["user_input"].append(input_data)

    graph = GenerationGraph(mode=mode, local_model_cfg=local_model_cfg)
    STATE = graph(STATE)
    last = STATE["last"][-1][1]
    output = STATE["agents_result"][last][-1]["content"]
    if last in ["x6processor", "editor"]:
        output = x6_layout(output)
    return GenerationOutput(output=output)


@router.post("/text", summary="Получить граф", response_model=GenerationOutput)
async def get_json_graph(user: GenerationInput) -> GenerationOutput:
    """
    :param input_data: Входные параметры для генерации диаграммы
    :return: BPMN диаграмма и дополнительная информация о процессе
    """

    return generate_output(user.user_input, 'api')
