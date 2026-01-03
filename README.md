https://www.kaggle.com/learn-guide/5-day-agents

---
# Google 5 Day Agents
## Day 1

### First Agent with ADK
#### Source Code
- [Kaggle Link](https://www.kaggle.com/code/kaggle5daysofai/day-1a-from-prompt-to-action)
- [Local Ipynb](./day1/day1a-single-agent.ipynb)

#### Code Explaination
1. Define Agent  
    **_`google.adk.agents.Agent` Class_**
    - name : 에이전트 이름
    - model : 모델 구성 (`google.adk.models.~` 하단의 model 관련 class 객체)
    - instruction : 에이전트의 역할과 사용법을 명시. 멀티 에이전트인 경우 매우 중요한 속성이 될 수 있음
    - tools : 에이전트가 사용할 도구 (기타 에이전트, 외부 API 등)
    - output_key : 에이전트의 출력 결과를 저장할 key. 주로 멀티 에이전트에서 에이전트끼리 구분하기 위해 사용함
2. Run Agent

#### CLI
1. Create agent
```bash
export GOOGLE_API_KEY=<YOUR_API_KEY>
adk create day1/sample_agent --model gemini-2.5-flash-lite --api_key $GOOGLE_API_KEY
```

2. Run agent on web
```bash
adk web day1
```

### Multi-Agent Systems & Workflow Pattern

|          | Single Agent                     | Multi Agent            |
|----------|----------------------------------|------------------------|
| 복잡도      | **낮음** : 디버깅, 개발, 관리가 쉬움  | **높음**                |
| 비용      | 쌈                               | 비쌈                    |
| Workflow | 순차적인 작업 수행                   | 병렬 작업 수행               |
| Use Case | 개발, 테스트, 디버깅                 | 복잡한 시나리오, 대규모 프로젝트 |
| 정확도     | 복잡한 작업 시 halluciation 위험도 높음| 높은 성능 기대할 수 있음      |

#### Source Code
- [Kaggle Link](https://www.kaggle.com/code/kaggle5daysofai/day-1b-agent-architectures)
- [Local Ipynb](./day1/day1b-multi-agent.ipynb)
