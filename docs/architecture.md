# System Architecture – Enterprise Decision Intelligence AI Platform (EDIP)

## 1. High-Level Overview
EDIP is a secure, cloud-native, multi-agent AI platform designed to transform unstructured enterprise data into verified, executive-ready insights.

The system follows a modular architecture with clear separation of concerns across frontend, backend, AI orchestration, data storage, and infrastructure layers.

---

## 2. Architecture Components

### Frontend (Client Layer)
- Built using Next.js and TypeScript
- Provides a secure user interface for submitting business queries
- Displays structured research reports with citations
- Handles user authentication via Clerk

### Backend (Application Layer)
- Built using FastAPI
- Acts as the orchestration layer between frontend and AI services
- Manages request validation, session handling, and authorization

### AI Orchestration Layer
- Implemented using LangGraph
- Coordinates multiple specialized agents:
  - Planner Agent
  - Research Agent
  - RAG Agent
  - Validator Agent
  - Writer Agent
  - Audit Agent

### Data Layer
- PostgreSQL: stores users, sessions, reports, and audit logs
- ChromaDB: stores vector embeddings for semantic search

### External Services
- Google Gemini Pro for text generation
- Tavily API for live web search
- YouTube Transcript API (optional)

---

## 3. Request Flow

1. User submits a business question via the frontend
2. Backend validates the request and user session
3. Planner Agent decomposes the question into subtasks
4. Research Agent gathers information from web and documents
5. RAG Agent injects relevant context from vector storage
6. Validator Agent cross-checks facts and sources
7. Writer Agent generates a structured executive report
8. Audit Agent logs sources, decisions, and metadata
9. Final report is returned to the frontend

---

## 4. Security & Governance
- Authentication handled by Clerk
- Role-based access control
- User session isolation
- Audit logging for traceability and compliance

---

## 5. Scalability Considerations
- Stateless backend services
- Horizontal scaling via containerization
- Vector search optimized for large document sets
- Modular agent design for independent scaling

---

## 6. Design Trade-offs
- LangGraph chosen for explicit agent control over autonomous loops
- ChromaDB selected for fast local vector search
- FastAPI used for async performance and clarity

---

## 7. Future Enhancements
- Cost optimization layer
- Agent performance evaluation metrics
- Fine-grained role-based agents
