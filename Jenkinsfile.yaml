pipeline:
  agent:
    any
  stages:
    - stage: Install Dependencies
      steps:
        - shell: pip install -r requirements.txt
    - stage: Run Tests
      steps:
        - shell: pytest tests/
    - stage: Run Application
      steps:
        - shell: python3 calendar_app.py
  post:
    always:
      - shell: echo "Pipeline execution completed!"
    success:
      - shell: echo "Pipeline executed successfully!"
    failure:
      - shell: echo "Pipeline failed. Check logs for details."
