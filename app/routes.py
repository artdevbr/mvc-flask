from mvc_flask import Router

Router.all("users")
Router.all("messages", only="index show new create")
