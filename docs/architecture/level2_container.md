# Level 2: Container Diagram

```mermaid
graph TD
User((Professor))

subgraph Faculty Portal System
UI[Web Application <br/> (React.js)]
API[API Gateway <br/> (Python FastAPI)]
DB[(Primary Database <br/> (PostgreSQL))]
end

AD[Active Directory]
Canvas[Canvas LMS API]

%% Relationships
User -->|HTTPS Request| UI
UI -->|JSON/REST| API
API -->|SQL Queries| DB

API -->|LDAP Auth| AD
API -->|REST| Canvas

%% Styling
style UI fill:#fbbf24,color:#000
style API fill:#fbbf24,color:#000
style DB fill:#004b23,color:#fff