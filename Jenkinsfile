pipeline:
  agent: any
  stages:
    - stage: "Install Dependencies"
      steps:
        - sh: pip install -r requirements.txt
    - stage: "Run Tests"
      steps:
        - sh: pytest tests/
    - stage: "Run Application"
      steps:
        - sh: python3 calendar_app.py
