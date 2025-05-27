"""
Handler registration central point.
"""
from .text_generation import TextGenerationHandler
from .task_management import TaskManagementHandler
from .user_interaction import UserInteractionHandler

def register_handlers(app):
    TextGenerationHandler(app).register()
    TaskManagementHandler(app).register()
    UserInteractionHandler(app).register()
