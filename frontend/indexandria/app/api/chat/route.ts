import { Humanloop, ChatMessageWithToolCall } from "humanloop";

if (!process.env.HUMANLOOP_API_KEY) {
  throw Error(
    "no Humanloop API key provided; add one to your .env.local file with: `HUMANLOOP_API_KEY=..."
  );
}

const humanloop = new Humanloop({
  basePath: "https://api.humanloop.com/v4",
  apiKey: process.env.HUMANLOOP_API_KEY,
});

export async function POST(req: Request): Promise<Response> {
  const messages: ChatMessageWithToolCall[] = (await req.json()) as ChatMessageWithToolCall[];

  const response = await humanloop.chatDeployedStream({
    project: "chat-tutorial-ts",
    messages,
  });

  return new Response(response.data);
}