from setuptools import setup, find_packages

setup(
    name="ai_telegram_bot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot>=20.0",
        "openai>=0.27.0",
        "python-dotenv>=1.0.0",
        "redis>=4.5.0",
    ],
    entry_points={
        "console_scripts": [
            "run-bot=run_bot:main",
        ],
    },
)
