openapi: 3.0.0
info:
  title: User API
  description: Простое API для управления пользователями
  version: 1.0.0

servers:
  - url: http://localhost:8000/api

paths:
  /users:
    get:
      summary: Получить список пользователей
      responses:
        '200':
          description: Успешный ответ
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'

    post:
      summary: Создать нового пользователя
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
      responses:
        '201':
          description: Пользователь создан

  /users/{id}:
    get:
      summary: Получить пользователя по ID
      parameters:
        - in: path
          name: id
          schema:
            type: integer
          required: true
      responses:
        '200':
          description: Данные пользователя
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'

    delete:
      summary: Удалить пользователя
      parameters:
        - in: path
          name: id
          schema:
            type: integer
          required: true
      responses:
        '204':
          description: Пользователь удалён

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
        email:
          type: string

