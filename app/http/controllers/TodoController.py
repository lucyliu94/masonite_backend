""" A TodoController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Todo import Todo



class TodoController(Controller):
    """Class Docstring Description
    """
    
    def __init__(self, request: Request):
        self.request = request
        
        

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", TodoController)
        """
        id = self.request.param("id")
        return Todo.find(id)

        pass

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", TodoController)
        """
        return Todo.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", TodoController)
        """
        subject = self.request.input("subject")
        details = self.request.input("details")
        todo = Todo.create({"subject": subject, "details": details})
        return todo

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", TodoController)
        """
        subject = self.request.input("subject")
        details = self.request.input("details")
        id = self.request.param("id")
        Todo.where("id", id).update({"subject": subject, "details": details})
        return Todo.where("id", id).get()
        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", TodoController)
        """
        id = self.request.param('id')
        todo = Todo.where("id", id).get()
        Todo.where("id", id).delete()
        return todo

        pass