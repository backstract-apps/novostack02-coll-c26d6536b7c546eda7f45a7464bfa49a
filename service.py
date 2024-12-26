from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def delete_nscollection(db: Session):
    res = {
    }
    return res

