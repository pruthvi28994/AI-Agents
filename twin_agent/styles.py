"""Styling constants for the portfolio Gradio chatbot.

Palette (from mywebsite-pruthvi.vercel.app):
    primary   #cc005f
    secondary #990047
    dark      #000000
    light     #f4f4f4
Font: Poppins

Usage:
    import gradio as gr
    from styles import CSS, JS

    with gr.Blocks(css=CSS, js=JS) as demo:
        gr.ChatInterface(your_chat_fn)

    demo.launch()
"""

PRIMARY = "#cc005f"
SECONDARY = "#990047"
DARK = "#000000"
LIGHT = "#f4f4f4"

EXAMPLES = [
    "Tell me about your background and experience.",
    "What projects have you worked on recently?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');

:root {
  --pf-primary: #cc005f;
  --pf-secondary: #990047;
  --pf-bg: #050505;
  --pf-surface: #0d0d0d;
  --pf-surface-2: #17171a;
  --pf-border: rgba(244, 244, 244, 0.10);
  --pf-border-strong: rgba(244, 244, 244, 0.20);
  --pf-text: #f4f4f4;
  --pf-muted: #9a9a9a;

  /* ---- Override Gradio's own theme tokens ----
     Gradio paints most surfaces (block backgrounds, inputs, the
     chatbot toolbar, the scroll-to-bottom button) directly from
     these CSS custom properties rather than fixed classes, so
     resetting them here is what actually kills the white panels,
     regardless of which Gradio version's markup you're on. */
  --body-background-fill: var(--pf-bg) !important;
  --body-text-color: var(--pf-text) !important;
  --background-fill-primary: var(--pf-surface) !important;
  --background-fill-secondary: var(--pf-surface-2) !important;
  --border-color-primary: var(--pf-border) !important;
  --border-color-accent: var(--pf-primary) !important;
  --block-background-fill: var(--pf-surface) !important;
  --block-border-color: var(--pf-border) !important;
  --block-label-background-fill: transparent !important;
  --block-label-text-color: var(--pf-muted) !important;
  --block-title-text-color: var(--pf-text) !important;
  --input-background-fill: transparent !important;
  --input-border-color: var(--pf-border) !important;
  --input-placeholder-color: rgba(244, 244, 244, 0.4) !important;
  --panel-background-fill: var(--pf-surface) !important;
  --panel-border-color: var(--pf-border) !important;
  --color-accent: var(--pf-primary) !important;
  --color-accent-soft: rgba(204, 0, 95, 0.15) !important;
  --button-primary-background-fill: var(--pf-primary) !important;
  --button-primary-background-fill-hover: var(--pf-secondary) !important;
  --button-primary-text-color: #ffffff !important;
  --button-secondary-background-fill: transparent !important;
  --button-secondary-border-color: var(--pf-border) !important;
  --button-secondary-text-color: var(--pf-text) !important;
  --neutral-50: var(--pf-surface-2) !important;
  --neutral-100: var(--pf-surface-2) !important;
  --neutral-800: var(--pf-text) !important;
  --neutral-900: var(--pf-text) !important;
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

html, body, gradio-app, .gradio-container, .app {
  background: var(--pf-bg) !important;
}

/* Subtle vignette for a less flat, more "designed" backdrop */
body::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  background:
    radial-gradient(ellipse 800px 500px at 50% -10%, rgba(204, 0, 95, 0.10), transparent 60%),
    radial-gradient(ellipse 600px 400px at 100% 100%, rgba(153, 0, 71, 0.08), transparent 60%);
  z-index: 0;
}

/* ---------- Layout ---------- */
.gradio-container {
  background: var(--pf-bg) !important;
  color: var(--pf-text) !important;
  font-family: 'Poppins', sans-serif !important;
  width: 100% !important;
  max-width: 880px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 32px 24px 48px !important;
}
.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}
.gradio-container * { min-width: 0; font-family: 'Poppins', sans-serif !important; }

/* ---------- Title (serif, luxury feel) ---------- */
.gradio-container h1 {
  font-family: 'Playfair Display', 'Poppins', serif !important;
  font-size: 32px !important;
  font-weight: 700 !important;
  letter-spacing: -0.01em !important;
  color: var(--pf-text) !important;
  border-left: 3px solid var(--pf-primary);
  padding-left: 16px !important;
  padding-bottom: 10px !important;
  margin: 4px 0 10px !important;
  text-align: left !important;
  position: relative !important;
  display: inline-block !important;
}

/* Thin gradient accent line under the title — decorative only,
   never risks the text itself going invisible. */
.gradio-container h1::after {
  content: "";
  position: absolute;
  left: 16px;
  bottom: 0;
  height: 2px;
  width: 64px;
  background: linear-gradient(90deg, var(--pf-primary), var(--pf-secondary), transparent);
  border-radius: 2px;
}

.gradio-container h1 + p,
.gradio-container .prose > p:first-of-type {
  color: var(--pf-muted) !important;
  font-size: 14px !important;
  letter-spacing: 0.02em;
}

/* ---------- Chatbot frame ---------- */
.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

.chatbot, .chatbot.block {
  background: var(--pf-surface) !important;
  border: 1px solid var(--pf-border) !important;
  border-radius: 18px !important;
  min-height: 460px !important;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(244, 244, 244, 0.03) inset !important;
  overflow: hidden !important;
}
.chatbot .placeholder, .chatbot .placeholder * { color: var(--pf-muted) !important; }

/* Safety net: kill any remaining white/light surfaces inside the chatbot
   from Gradio's own wrapper divs, whatever they're called this version.
   Bubble backgrounds below are more specific, so they still win. */
.chatbot, .chatbot * {
  background-color: transparent;
}
.chatbot, .chatbot.block { background-color: var(--pf-surface) !important; }

/* ---------- Toolbar (share / delete / copy) + scroll-to-bottom button ----------
   These render as separate floating icon buttons layered over the chat,
   painted white by Gradio's default button theme. */
.chatbot button,
.chatbot [class*="button"],
.message-buttons-left button,
.message-buttons-right button,
.scroll-down-button,
button[aria-label="Scroll down"] {
  background: rgba(23, 23, 26, 0.85) !important;
  backdrop-filter: blur(6px);
  border: 1px solid var(--pf-border-strong) !important;
  color: var(--pf-muted) !important;
  border-radius: 8px !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4) !important;
}
.chatbot button:hover,
.chatbot [class*="button"]:hover,
.message-buttons-left button:hover,
.message-buttons-right button:hover,
.scroll-down-button:hover {
  border-color: var(--pf-primary) !important;
  color: var(--pf-primary) !important;
  background: rgba(23, 23, 26, 0.95) !important;
}
.chatbot button svg,
.chatbot [class*="button"] svg,
.scroll-down-button svg {
  color: inherit !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* ---------- Message rows: strip parent backgrounds ---------- */
.message-row,
.message-row > div,
.message-row .role,
.message-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

/* Reset borders on every bubble variant first */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble,
.message.user, .message.bot {
  border: 0 !important;
  box-shadow: none !important;
  padding: 10px 14px !important;
}

/* ---------- Bubble backgrounds: covers both old (.message.user/.bot)
   and new (.message-row[data-role]) Gradio markup ---------- */
.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble,
.message.user, .message-wrap .user {
  background: var(--pf-primary) !important;
  color: #ffffff !important;
  border-radius: 14px 14px 2px 14px !important;
}

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble,
.message.bot, .message-wrap .bot {
  background: var(--pf-surface-2) !important;
  color: var(--pf-text) !important;
  border-radius: 14px 14px 14px 2px !important;
  border: 1px solid var(--pf-border) !important;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.35) !important;
}

/* ---------- Uniform bubble typography ---------- */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble,
.message.user, .message.bot {
  font-size: 14px !important;
  line-height: 1.55 !important;
}
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p,
.message.user p, .message.bot p {
  font-size: 14px !important;
  line-height: 1.55 !important;
  margin: 0 0 8px !important;
  color: inherit !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child,
.message.user p:last-child, .message.bot p:last-child { margin-bottom: 0 !important; }

/* Strip stray internal borders/backgrounds inside a bubble, keep link accent */
.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble *,
.message.user *, .message.bot * {
  background: transparent !important;
  border-color: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}
.message-row .message a,
.message-row .message-bubble a,
.message.bot a {
  color: var(--pf-primary) !important;
  text-decoration: underline;
}

/* ---------- Inputs (underline style, like your contact form) ---------- */
textarea, input[type="text"], input[type="email"] {
  background: transparent !important;
  border: none !important;
  border-bottom: 1px solid var(--pf-border) !important;
  border-radius: 0 !important;
  color: var(--pf-text) !important;
  font-size: 14px !important;
  padding: 12px 4px !important;
  line-height: 1.4 !important;
  min-height: 48px !important;
}
textarea:focus, input[type="text"]:focus, input[type="email"]:focus {
  border-bottom: 1px solid var(--pf-primary) !important;
  outline: none !important;
  box-shadow: none !important;
}
textarea::placeholder, input::placeholder { color: rgba(244, 244, 244, 0.45) !important; }

/* ---------- Buttons ---------- */
button {
  font-family: 'Poppins', sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  border: 1px solid var(--pf-border) !important;
  background: transparent !important;
  color: var(--pf-text) !important;
  border-radius: 6px !important;
  padding: 0 16px !important;
  min-height: 46px !important;
  cursor: pointer;
  transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease, transform 0.15s ease;
}
button:hover { border-color: var(--pf-primary) !important; color: var(--pf-primary) !important; }

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background: var(--pf-primary) !important;
  border: 1px solid var(--pf-primary) !important;
  color: #ffffff !important;
}
button.primary:hover,
button.submit:hover,
.submit-button:hover,
button.lg.primary:hover {
  background: var(--pf-secondary) !important;
  border-color: var(--pf-secondary) !important;
  color: #ffffff !important;
  transform: translateY(-1px);
}

button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg {
  width: 18px !important;
  height: 18px !important;
  color: #ffffff !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* ---------- Examples ---------- */
.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding: 0 !important;
  margin-top: 14px !important;
}
.examples table, .examples-table { background: transparent !important; border: 0 !important; }
.examples button, .example, .examples td button, [data-testid="examples"] button {
  background: var(--pf-surface) !important;
  border: 1px solid var(--pf-border) !important;
  color: var(--pf-text) !important;
  font-weight: 400 !important;
  font-size: 13px !important;
  padding: 10px 14px !important;
  text-align: left !important;
  min-height: 0 !important;
}
.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: var(--pf-primary) !important;
  color: var(--pf-primary) !important;
}

/* ---------- Icon buttons (clear, retry, copy) ---------- */
.icon-button, .chatbot .icon-button {
  color: var(--pf-muted) !important;
  background: transparent !important;
  border: 0 !important;
  min-height: 0 !important;
  padding: 4px !important;
}
.icon-button:hover, .chatbot .icon-button:hover { color: var(--pf-primary) !important; }

/* ---------- Scrollbar ---------- */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: var(--pf-bg); }
::-webkit-scrollbar-thumb { background: var(--pf-primary); border-radius: 8px; }
::-webkit-scrollbar-thumb:hover { background: var(--pf-secondary); }
* { scrollbar-width: thin; scrollbar-color: var(--pf-primary) var(--pf-bg); }

/* ---------- Selection ---------- */
::selection { background: var(--pf-primary); color: #ffffff; }

/* ---------- Mobile ---------- */
@media (max-width: 640px) {
  .gradio-container { padding: 22px 14px 36px !important; }
  .gradio-container h1 { font-size: 22px !important; }
}
"""

JS = """
() => {
  document.title = 'Chat with Pruthvi';

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  // Re-focus the message field whenever Gradio re-enables it
  // (i.e. right after the assistant finishes responding).
  const watchTextarea = (area) => {
    if (area.dataset.pfWatched) return;
    area.dataset.pfWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  // Auto-scroll the chatbot to the latest message as new content streams in.
  const watchChatScroll = () => {
    const chatEl = document.querySelector('.chatbot .wrap, .chatbot .scroll, .chatbot');
    if (!chatEl || chatEl.dataset.pfScrollWatched) return;
    chatEl.dataset.pfScrollWatched = '1';
    const scrollToBottom = () => { chatEl.scrollTop = chatEl.scrollHeight; };
    new MutationObserver(scrollToBottom).observe(chatEl, { childList: true, subtree: true });
  };

  const scan = () => {
    document.querySelectorAll('textarea').forEach(watchTextarea);
    watchChatScroll();
  };
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""