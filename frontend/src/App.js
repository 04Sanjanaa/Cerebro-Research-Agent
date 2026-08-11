import React, { useState, useEffect, useRef } from 'react';
import { Search, FileText, BarChart3, Clock, BookOpen, AlertCircle, CheckCircle, ChevronDown, ChevronUp, Loader } from 'lucide-react';
import api from './services/api';
import './index.css';

const EXAMPLE_QUESTIONS = [
  'What is the annual leave entitlement?',
  'How far in advance must leave be requested?',
  'What are the remote work eligibility requirements?',
  'What are the password complexity requirements?',
  'What is the expense reimbursement limit for meals?',
  'How do leave and remote work policies interact?',
];

function CitationCard({ citation, expanded, onToggle }) {
  return (
    <div className="citation-card">
      <div className="citation-header" onClick={onToggle}>
        <span className="citation-badge">[{citation.id}]</span>
        <div className="citation-meta">
          <span className="citation-source">{citation.source}</span>
          {citation.section && <span className="citation-section"> — {citation.section}</span>}
          <span className={`citation-score score-${citation.relevance?.toLowerCase().replace(' ', '-')}`}>
            {citation.relevance} ({(citation.score * 100).toFixed(0)}%)
          </span>
        </div>
        <button className="expand-btn">{expanded ? <ChevronUp size={14}/> : <ChevronDown size={14}/>}</button>
      </div>
      {expanded && (
        <div className="citation-passage">
          <p>{citation.passage}</p>
          <small className="chunk-id">Chunk: {citation.chunk_id}</small>
        </div>
      )}
    </div>
  );
}

function MessageBubble({ msg }) {
  const [expandedCitations, setExpandedCitations] = useState({});
  const toggleCitation = (id) => setExpandedCitations(prev => ({ ...prev, [id]: !prev[id] }));

  if (msg.role === 'user') {
    return (
      <div className="message user-message">
        <div className="message-bubble user-bubble">
          <p>{msg.content}</p>
          <span className="msg-time">{msg.timestamp}</span>
        </div>
      </div>
    );
  }

  return (
    <div className="message assistant-message">
      <div className="message-icon"><BookOpen size={18}/></div>
      <div className="message-content">
        {msg.insufficient ? (
          <div className="insufficient-notice">
            <AlertCircle size={18} className="insuf-icon"/>
            <div>
              <strong>Insufficient Evidence</strong>
              <p>{msg.content}</p>
            </div>
          </div>
        ) : (
          <div className="answer-text">
            {msg.content.split('\n').map((line, i) => (
              <p key={i} dangerouslySetInnerHTML={{ __html: line
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                .replace(/\[(\d+)\]/g, '<span class="inline-cite">[$1]</span>') || '<br/>'
              }} />
            ))}
          </div>
        )}

        {msg.citations && msg.citations.length > 0 && (
          <div className="citations-section">
            <div className="citations-title">
              <CheckCircle size={14}/> Sources & Evidence
              <span className="retrieval-info">
                {msg.retrieval?.chunks_retrieved} passages retrieved · {msg.retrieval?.sources_used} source{msg.retrieval?.sources_used !== 1 ? 's' : ''}
                {msg.model && msg.model !== 'keyword_fallback' && ` · ${msg.model}`}
              </span>
            </div>
            {msg.citations.map(c => (
              <CitationCard
                key={c.id}
                citation={c}
                expanded={!!expandedCitations[c.id]}
                onToggle={() => toggleCitation(c.id)}
              />
            ))}
          </div>
        )}
        <span className="msg-time">{msg.timestamp}</span>
      </div>
    </div>
  );
}

export default function App() {
  const [tab, setTab] = useState('chat');
  const [query, setQuery] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [docs, setDocs] = useState([]);
  const [logs, setLogs] = useState([]);
  const [stats, setStats] = useState(null);
  const [error, setError] = useState(null);
  const bottomRef = useRef(null);

  useEffect(() => { fetchAll(); }, []);
  useEffect(() => { bottomRef.current?.scrollIntoView({ behavior: 'smooth' }); }, [messages]);

  const fetchAll = async () => {
    try {
      const [d, l, s] = await Promise.all([
        api.get('/api/documents'),
        api.get('/api/logs'),
        api.get('/api/stats'),
      ]);
      if (d.data.success) setDocs(d.data.documents);
      if (l.data.success) setLogs(l.data.logs);
      if (s.data.success) setStats(s.data.stats);
    } catch (e) { setError('Could not connect to backend.'); }
  };

  const sendQuery = async (q) => {
    const question = q || query;
    if (!question.trim()) return;
    setMessages(prev => [...prev, { role: 'user', content: question, timestamp: new Date().toLocaleTimeString() }]);
    setQuery('');
    setLoading(true);
    setError(null);
    try {
      const res = await api.post('/api/research', { query: question });
      const d = res.data;
      setMessages(prev => [...prev, {
        role: 'assistant',
        content: d.answer,
        citations: d.citations,
        retrieval: d.retrieval_info,
        insufficient: d.insufficient_evidence,
        model: d.model_used,
        timestamp: new Date().toLocaleTimeString(),
      }]);
      setTimeout(fetchAll, 500);
    } catch (e) {
      setError(e.response?.data?.error || 'Request failed');
    } finally { setLoading(false); }
  };

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-brand">
          <div className="brand-icon"><BookOpen size={22}/></div>
          <div>
            <h1>CEREBRO</h1>
            <span className="brand-sub">Research Agent with Citations</span>
          </div>
        </div>
        <div className="header-status">
          {stats && (
            <>
              <span className="status-pill">{stats.retrieval_mode === 'semantic' ? '⚡ Semantic' : '🔤 TF-IDF'}</span>
              <span className="status-pill">{stats.llm_enabled ? `🤖 ${stats.llm_model}` : '📝 Keyword'}</span>
              <span className="status-pill">📚 {stats.total_chunks} chunks</span>
            </>
          )}
        </div>
      </header>

      <nav className="app-nav">
        {[['chat','💬 Research'], ['documents','📄 Documents'], ['logs','📋 Logs'], ['stats','📊 Stats']].map(([id, label]) => (
          <button key={id} className={`nav-btn ${tab===id?'active':''}`} onClick={() => setTab(id)}>{label}</button>
        ))}
      </nav>

      <main className="app-main">
        {error && <div className="error-banner"><AlertCircle size={16}/> {error}</div>}

        {tab === 'chat' && (
          <div className="chat-layout">
            <div className="chat-messages">
              {messages.length === 0 && (
                <div className="welcome">
                  <div className="welcome-icon">🔬</div>
                  <h2>Research Agent</h2>
                  <p>Ask a question. The agent retrieves relevant passages from the knowledge base and answers with citations — or tells you when the evidence is insufficient.</p>
                  <div className="example-questions">
                    {EXAMPLE_QUESTIONS.map(q => (
                      <button key={q} className="example-q" onClick={() => sendQuery(q)}>{q}</button>
                    ))}
                  </div>
                </div>
              )}
              {messages.map((m, i) => <MessageBubble key={i} msg={m}/>)}
              {loading && (
                <div className="message assistant-message">
                  <div className="message-icon"><BookOpen size={18}/></div>
                  <div className="loading-dots"><Loader size={16} className="spin"/><span>Retrieving evidence...</span></div>
                </div>
              )}
              <div ref={bottomRef}/>
            </div>
            <div className="chat-input-area">
              <input
                className="chat-input"
                placeholder="Ask a research question..."
                value={query}
                onChange={e => setQuery(e.target.value)}
                onKeyDown={e => e.key === 'Enter' && !e.shiftKey && sendQuery()}
                disabled={loading}
              />
              <button className="send-btn" onClick={() => sendQuery()} disabled={loading || !query.trim()}>
                <Search size={18}/>
              </button>
            </div>
          </div>
        )}

        {tab === 'documents' && (
          <div className="panel">
            <h2>Knowledge Base Documents</h2>
            <p className="panel-desc">{docs.length} document{docs.length !== 1 ? 's' : ''} indexed · {stats?.total_chunks || 0} chunks total</p>
            <div className="doc-grid">
              {docs.map((d, i) => (
                <div key={i} className="doc-card">
                  <div className="doc-icon"><FileText size={24}/></div>
                  <h3>{d.source}</h3>
                  <p>{d.chunk_count} chunks</p>
                  {d.sections?.slice(0,3).map((s,j) => s && <span key={j} className="section-tag">{s.slice(0,40)}</span>)}
                </div>
              ))}
            </div>
            <button className="reload-btn" onClick={() => api.post('/api/reload').then(fetchAll)}>↻ Reload Knowledge Base</button>
          </div>
        )}

        {tab === 'logs' && (
          <div className="panel">
            <h2>Query Logs</h2>
            <div className="log-list">
              {logs.length === 0 && <p className="empty">No queries yet.</p>}
              {logs.map((l, i) => (
                <div key={i} className={`log-item ${l.answered ? 'answered' : 'unanswered'}`}>
                  <span className={`log-status ${l.answered ? 'ok' : 'warn'}`}>{l.answered ? '✓' : '?'}</span>
                  <div className="log-body">
                    <p className="log-query">{l.query}</p>
                    <small>{new Date(l.timestamp).toLocaleString()} · {l.sources?.length || 0} sources</small>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {tab === 'stats' && stats && (
          <div className="panel">
            <h2>System Statistics</h2>
            <div className="stats-grid">
              {Object.entries({
                'Total Documents': stats.total_documents,
                'Total Chunks': stats.total_chunks,
                'Total Queries': stats.total_queries,
                'Answered': stats.answered_queries,
                'Unanswered': stats.unanswered_queries,
                'Response Rate': stats.response_rate,
                'Retrieval Mode': stats.retrieval_mode,
                'LLM Enabled': stats.llm_enabled ? `Yes (${stats.llm_model})` : 'No (keyword fallback)',
                'Min Score Threshold': stats.min_score_threshold,
              }).map(([k, v]) => (
                <div key={k} className="stat-card"><span className="stat-label">{k}</span><span className="stat-value">{String(v)}</span></div>
              ))}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
