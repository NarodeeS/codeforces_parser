from schemas import TaskSchema


def prepare_task_message(task: TaskSchema) -> str:
    message = f'<b>{task.title}</b>\n\n'
    message += f'Номер задания: {task.number}\n'
    message += f'Количество решений: {task.solved_count}\n'
    message += f'Сложность: {task.difficulty.value}\n'
    message += f'Темы: {", ".join([theme.description for theme in task.themes])}'
    return message
