import web

render = web.template.render('views')

class formulario:
    def GET(self):
        try:
            return render.formulario()
        except Exception as e:
            return "Error "+str(e.args)