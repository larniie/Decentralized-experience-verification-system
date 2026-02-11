# Decentralized Experience Verification System (DEVS)

## Overview
DEVS is a decentralized system for verifying experiences using blockchain technology. It provides a secure and transparent way to store and verify professional or personal experiences.

## Architecture
- Client (Frontend): User interface for interacting with the system.
- API Gateway (Flask): Entry point for API requests, built with Flask.
- Service Layer: Business logic for handling identities, experiences, and blockchain operations.
- Domain Layer: Core business objects like Identity, Experience, and Block.
- Persistence Layer: Data storage and retrieval, including ledger repository.

## Setup
1. Install dependencies: `pip install -r backend/requirements.txt`
2. Run the backend: `python backend/app.py`
3. Open `frontend/verify.html` in a browser to access the frontend.

## API Endpoints
- `/api/identity`: Manage identities
- `/api/experience`: Manage experiences
- `/api/ledger`: Interact with the blockchain ledger

## Technologies
- Backend: Flask, Python
- Frontend: HTML, JavaScript
- Blockchain: Custom implementation
