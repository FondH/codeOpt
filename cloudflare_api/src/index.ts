import { Ai } from '@cloudflare/ai';

export interface Env {
  AI: any;
}

export default {
  async fetch(request: Request, env: Env) {
    const url = new URL(request.url);
    const path = url.pathname;

    const ai = new Ai(env.AI);

    if (path === '/api' && request.method === 'POST') {
      const formData = await request.formData();
      const userQuestion = formData.get('question') || '';
      const systemPrompt = formData.get('system') || 'You are a friendly assistant';

      const messages = [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userQuestion }
      ];
      const response = await ai.run('@cf/meta/llama-3-8b-instruct', { messages });

      return new Response(JSON.stringify({ response: response.response }), { headers: { 'Content-Type': 'application/json' } });
    }




    
    return new Response(`
      <!DOCTYPE html>
      <html>
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
          h1 {
            text-align: center;
          }
          form {
            width: 80%;
            margin: 0 auto;
          }
          label {
            display: block;
            text-align: center;
          }
          input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            box-sizing: border-box;
          }
          input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            box-sizing: border-box;
            background-color: initial;
          }
          #response {
            width: 80%;
            margin: 0 auto;
          }
        </style>
      </head>
      <body>
        <h1>Llama-2-7b LLM Answerer</h1>
        <form id="question-form">
          <label for="question">Input a Question:</label>
          <input type="text" id="question" name="question">
          <label for="system">System Prompt:</label>
          <input type="text" id="system" name="system" value="You are a friendly assistant">
          <input type="submit" value="Submit" id="submit-button">
        </form>
        <div id="response"></div>
        <script>
          document.querySelector('#question-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const submitButton = document.getElementById('submit-button');
            
            submitButton.style.backgroundColor = 'lightcyan';
            submitButton.disabled = true;

            const response = await fetch('/api', { method: 'POST', body: formData });
            const data = await response.json();
            document.getElementById('response').innerHTML = data.response;

            submitButton.style.backgroundColor = 'initial';
            submitButton.disabled = false;
          });
        </script>
      </body>
      </html>
    `, { headers: { 'Content-Type': 'text/html' } });
  },
};
