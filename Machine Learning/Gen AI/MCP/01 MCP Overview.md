## What is MCP?

MCP is a communication layer that provides LLMs with context and tools without requiring us to write a bunch of tedious code.

## The Problem MCP Solves
Let's say we want to build a chatbot that can answer questions about Github repositories.
Ex: What open pull requests are there across all my repositories?

Without MCP, we would need to write a lot of tools schemas and functions to handle all of Github's features.

With MCP, it shifts this burden by moving tool definition and execution from our server to dedicated MCP servers of Github. Instead of authoring all those Github tools, an MCP server for Github handles it.

The MCP Server wraps up tons of functionality around Github and exposes it as a standardised set of tools.
Our application connects to this server instead of implementing everything from scratch.

## What is MCP Server?
MCP servers provided access to data or functionality implemented by outside services. They act as specialised interfaces that expose tools, prompts, and resource in a standardised way.


## What is MCP Client?
The MCP client serves as the communication bridge between your server and MCP servers.
It is the access point to all the tools that an MCP server provides, handling the message exchange and protocol details so your application doesn't have to.

## How does MCP Client communicate with MCP Server?
Transport Agnostic Communication
- Clients and Server can communicate over different Protocol depending on the Setup.
- Standard IO: If Client and Server are running on a same machine
- HTTP, WebSockets, etc: If Client and Server are running on different machines


MCP Message Type:
Clients and Server exchange messages of the following types:
- ListToolsRequest: Give me a list of tools you provide. (Client to Server)
- ListToolsResults: Here are the tools I can run. (Server to Client)
- CallToolRequest: Please execute this tool with these arguments. (Client to Server)
- CallToolResult: Here is the result of the tool execution. (Server to Client)


## Tools: LLM Controlled
- Tools are controlled entirely by LLMs. The AI Model decides when to call these tools.

## Resources: App Controlled
- Resources are controlled by your application. App decides when to fetch resource data and how to use it.
Typically for UI elements or to add Context to conversation.

## Prompts: User Controlled
- Prompts are triggered by the user actions. Users decide when to run these predefined workflows through UI interactions like button clicks, menu selections, or slash commands.
