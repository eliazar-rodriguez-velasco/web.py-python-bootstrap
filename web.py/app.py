from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web

urls = (
    '/', 'controllers.formulario.formulario'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
