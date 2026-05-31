RULES = {
    
    ".git": {
        "title": "Exposed Git Repository",
        "severity": "Critical",
        "score": 100,
        "recommendation": "Verify that the .git directory is not publicly accessible."
    },
    
    ".env": {
        "title": "Environment File Exposure",
        "severity": "Critical",
        "score": 100,
        "recommendation": "Sensitive configuration may be exposed."
    },
    
    "backup": {
        "title": "Backup File Exposure",
        "severity": "High",
        "score": 90,
        "recommendation": "Review exposed backup files."
    },
    
    "dump": {
        "title": "Database Dump Exposure",
        "severity": "High",
        "score": 90,
        "recommendation": "Database dumps should never be public."
    },
    
    "graphql": {
        "title": "GraphQL Endpoint Found",
        "severity": "High",
        "score": 80,
        "recommendation": "Review GraphQL schema exposure."
    },
    
    "swagger": {
        "title": "Swagger Documentation Found",
        "severity": "High",
        "score": 80,
        "recommendation": "Review exposed API documentation."
    },
    
    "api-docs": {
        "title": "API Documentation Found",
        "severity": "High",
        "score": 80,
        "recommendation": "Review exposed API documentation."
    },
    
    "redoc": {
        "title": "API Documentation Found",
        "severity": "High",
        "score": 80,
        "recommendation": "Review exposed API documentation."
    },
    
    "admin": {
        "title": "Administrative Interface Found",
        "severity": "Medium",
        "score": 50,
        "recommendation": "Review access controls."
    },
    
    "administrator": {
        "title": "Administrative Interface Found",
        "severity": "Medium",
        "score": 50,
        "recommendation": "Review access controls."
    },
    
    "dashboard": {
        "title": "Administrative Dashboard Found",
        "severity": "Medium",
        "score": 50,
        "recommendation": "Review dashboard access."
    },
    
    "login": {
        "title": "Login Portal Found",
        "severity": "Low",
        "score": 40,
        "recommendation": "Review authentication controls."
    },
    
    "portal": {
        "title": "Portal Found",
        "severity": "Low",
        "score": 40,
        "recommendation": "Review portal exposure."
    }
    
    }
    