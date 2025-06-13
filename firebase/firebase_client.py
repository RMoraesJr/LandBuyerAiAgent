"""Utility functions for interacting with Firebase Firestore."""

import firebase_admin
from firebase_admin import credentials, firestore


def init_firebase(cred_path: str) -> firestore.Client:
    """Initialize Firebase app and return a Firestore client."""
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    return firestore.client()
