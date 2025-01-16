from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()
SUPABASE_URL=os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.get("/{brand_name}/getproducts")
async def get_products_by_brand(brand_name: str):
    try:
        
        brand_name=brand_name.title()
        # print(brand_name)
        response = supabase.table("scrapedProducts").select("*").eq("brand", brand_name).execute()
        
        return {"brand": brand_name, "products": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get('/')
def index():
    return {"Details" : "Hello"}