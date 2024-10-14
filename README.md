# flask_prisma_project

### Running:
- Clone the repo
- Start Server: Run `python app.py` in project directory
- View data with Prisma Studio: Run `npx prisma studio` in project directory. Open the printed url.

### Resetting:
- Delete the `database.db` and `migrations` folder
- Run `prisma migrate dev --name init` in project directory