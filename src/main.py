from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

import config

from payload import text
from payload import seed
from util import resp


vesion = '2.0.0'
title = 'FSA'
desp = '善思-头像服务'

app = FastAPI(title=title, description=desp, version=vesion)

# #################
# 资源
app.mount("/assets", StaticFiles(directory=config.assetsdir), name="assets")
app.mount("/pages", StaticFiles(directory=config.pagesdir), name="pages")

# #################
# 跨域配置
origins = [
	"*",
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# #################
# Swagger文档资源本地化
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

# Windows/Mac下开发 才显示文档
import platform

#if (platform.system() == 'Darwin' or platform.system() == 'Windows'):
if 1:


	@app.get("/sd", include_in_schema=False)
	async def custom_swagger_ui_html():
		return get_swagger_ui_html(
			openapi_url=app.openapi_url,
			title=app.title + " - Swagger UI",
			oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
			swagger_js_url="/assets/doc/swagger-ui-bundle.js",
			swagger_css_url="/assets/doc/swagger-ui.css",
			swagger_favicon_url="/assets/doc/favicon.png",
		)


	@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
	async def swagger_ui_redirect():
		return get_swagger_ui_oauth2_redirect_html()


	@app.get("/rd", include_in_schema=False)
	async def redoc_html():
		return get_redoc_html(
			openapi_url=app.openapi_url,
			title=app.title + " - ReDoc",
			redoc_js_url="/assets/doc/redoc.standalone.js",
		)

# endif



# 文本
app.include_router(text.router, prefix="/text", tags=["文本"])

# 种子随机
app.include_router(seed.router, prefix="/seed", tags=["种子随机"])



# 主接口
@app.get(path="/{seed}")
async def generate(seed: str):

	filename = config.avatardir + "/default.png"

	
	return resp.resp_jpg(filename)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=9009, reload=True)
