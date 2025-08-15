#pip install -r requirements.txt
from fastapi import FastAPI,Request,Form,status,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fakemail.mail import main
from fakemail.inbox import messages
from typing import Any
app = FastAPI()
temp = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/",response_class=HTMLResponse,status_code=status.HTTP_200_OK)
async def index(request: Request) -> Any:
    data=main.gen().__str__()
    email=data["data"]["email"]
    return temp.TemplateResponse("index.html",{"request":request,"date":data,"inbox":messages.inboxs().__str__(email=email)})
@app.post("/new",response_class=HTMLResponse,status_code=status.HTTP_200_OK)
async def mail(request: Request) -> Any:
    data=main.gen().__str__()
    email=data["data"]["email"]    
    return temp.TemplateResponse("index.html",{"request":request,"date":data,"inbox":messages.inboxs().__str__(email=email)})
@app.get("/reload/{email}",response_class=HTMLResponse,status_code=status.HTTP_200_OK)
async def message(request: Request,email:str) -> Any:
    return temp.TemplateResponse("index.html",{"request":request,"inbox":messages.inboxs().__str__(email=email),"date":{"data":{"email":email}}})
# import java.util.Scanner;

# public class Main {
#     public static void main(String[] args) {
#         Scanner hh = new Scanner(System.in);
#         System.out.print("atro :");
#         String ntro = hh.nextLine(); 
#         System.out.println("atroo " + ntro); 
#     }
# }
