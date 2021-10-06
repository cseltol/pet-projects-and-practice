import express from 'express';
import mongoose from 'mongoose';
import router from './router.js'
import fileUpload from 'express-fileupload';

const PORT = 8080;
const DB_URl = `mongodb+srv://user:root@someback.j1qke.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`;
const app = express();

app.use(express.json())
app.use(express.static('static'))
app.use(fileUpload({}))
app.use('/api', router)

async function startApp() {
    try {
        await mongoose.connect(DB_URl, {useUnifiedTopology: true, useNewUrlParser: true});
        app.listen(PORT, () => console.log(`Server has been started on localhost:${PORT} !`));
    } catch (err) {
        console.log(err);
    }
};

startApp();