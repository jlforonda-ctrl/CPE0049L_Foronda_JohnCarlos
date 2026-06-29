# Level 1: System Context Diagram

```mermaid
graph TD
%% Define Actors and Systems
User((Professor))
System[Faculty Portal System]
AD[Active Directory]
Canvas[Canvas LMS API]

%% Define Relationships
User -->|Views schedules and submits grades| System
System -->|Authenticates via| AD
System -->|Pushes final grades to| Canvas

%% Styling
style System fill:#004b23,stroke:#fff,stroke-width:2px,color:#fff