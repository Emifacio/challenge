FROM node:18

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de configuración y de dependencias
COPY package*.json ./

# Instalar las dependencias
RUN npm install

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto que Vite usará
EXPOSE 5173

# Comando para correr la aplicación
CMD ["npm", "run", "dev"]
