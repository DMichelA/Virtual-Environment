import web 
import app 

render=web.template.render('mvc/views/')

class Formulario():

    def GET(self):
      try:
        return render.formulario() #renderizado formulario.html
      except Exception as e:
        return "Error" + str(e.args)