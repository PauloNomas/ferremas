class carrito:
      def __init__(self, request):
            self.request = request
            self. session = request.session
            carrito = self.session["carrito"]
            if not carrito:
                  self.session["carrito"] = {}
                  self.carrito = self.session["carrito"]
            else: 
                  self.carrito = carrito
            
      def agregar(self, producto):
            id = str(producto.id)
            if id not in self.carrito.keys():
                  self.carrito[id] = {
                        "producto_id": producto_id,
                        "nombre": producto.nombre,
                        "acumulado": prodcuto.precio,
                        "cantidad": 1,
                  }
            else:
                  self.carrito[id]["cantidad"] += 1
                  self.carrito[id]["acumulado"] += precio.producto
            self.guardar_carrito()

      def guardar_carrito(self):
            self.session["carrito"] = self.carrito
            self.session.modified = True

      def eliminar(self, producto):
            id = str(producto.id)
            if id in self.carrito[id]
            self.guardar_carrito()

      def restar(self.producto):
            id = str(producto.id)
            if id in self.carrito.keys():
                  self.carrito[id]["cantidad"] -=1
                  self.carrito[id]["acumulado"] -= producto.precio
                  if self.carrito[id]["cantidad"] <= 0_ self.eliminar(producto)
                  self.guardar_carrito()
      
      def limpiar(self):
            self.session["carrito"] ={}
            self.session.modified = True



