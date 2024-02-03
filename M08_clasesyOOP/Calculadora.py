class Calcular2:
    def __init__(self,lista_cl):
        if type (lista_cl) != list:
            raise ValueError("Se esperaba una lista de números enteros")
        else:    
            self.listacl = lista_cl

    def funpri(self):
        lista_primos = []
        for i in self.listacl:
            lista_primos.append(self.__funpri(i))
        return lista_primos
  

    def convgr (self,umo,umd):
        lisgr = []
        parames = ["F", "C", "K"]
        if str(umo) not in parames:
            print ("El parámetro en la unidad de origen no es el esperado, se esperaba:", parames)
        if str(umd) not in parames:
            print("El parámetro en la unidad de destino no es el esperado, se esperaba:", parames)
        else:     
            for f in self.listacl:
                vlgr = self.__convgr(f,umo,umd)
                lisgr.append (vlgr)
            return lisgr

    def funfac (self):
        lisfac = []
        for e in self.listacl:
            fact = self.__funfac(e)
            lisfac.append(fact)
        return lisfac
    
    def __funpri(self, nrv):
        primo = True
        if (type(nrv) == int):
            for x in range (2,nrv):
                if (nrv % x == 0) :
                    primo = False
                    break
        else:
            print ("ingrese un nro entero")
        return primo

    def funcrep (self):
        lisrep = []
        for elem in self.listacl:
            canrep = self.listacl.count(elem)
            lisrep.append(canrep)
            if self.listacl.count(elem) == max(lisrep):
                nromasrep = elem       
        mlis= max(lisrep)
        return nromasrep, mlis

    def __convgr (self, vl, umo, umd):
        if umo == "F" and umd == "C" :
            nvl = (vl - 32) / (9/5) 
        elif umo == "F" and umd == "K" :
            nvl = ((vl - 32) / (9/5)) + 273.15
        elif umo == "C" and umd == "F" :
            nvl = (vl * (9/5)) + 32
        elif umo == "C" and umd == "K" :
            nvl = vl + 273,15
        elif umo == "K" and umd == "F" :
            nvl = (vl - 273.15) * (9/5) +32
        elif umo == "K" and umd == "C" :
            nvl = vl - 273.15
        else:
            nvl = vl
        return nvl

    def __funfac (self, vlfac):
        if type (vlfac) == int:
            if vlfac > 0 :
                for xf in range (2,vlfac):
                    vlfac = vlfac * xf
                return vlfac
            else:
                print ("El nro ingresado no es positivo")
        else:
            print ("El valor ingresado no es un entero")  