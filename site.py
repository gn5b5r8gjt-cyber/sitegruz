<!DOCTYPE html>
<html lang="ru" data-lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nurtay — Биржа автоперевозок Казахстан</title>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&family=Unbounded:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root {
  --bg:#f0f4fb; --surface:#fff; --text:#18212f; --muted:#667085;
  --primary:#1f6feb; --primary-dark:#1356bb; --accent:#0f9d7a;
  --danger:#dc2626; --warn:#d97706; --border:#e5eaf2;
  --shadow:0 8px 28px rgba(16,24,40,.09); --shadow-lg:0 20px 60px rgba(16,24,40,.18);
  --violet:#7c3aed; --violet-dark:#5b21b6;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Nunito',sans-serif;color:var(--text);background:var(--bg);min-height:100vh}
.container{width:min(1160px,95%);margin:0 auto}


.topbar{background:#0f172a;color:#dbe3f0;border-bottom:1px solid rgba(255,255,255,.07)}
.topbar-inner{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding:10px 0;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:.75rem}
.brand-logo{width:38px;height:38px;border-radius:10px;display:grid;place-items:center;font-weight:800;font-size:1.1rem;background:linear-gradient(135deg,#1f6feb,#0f9d7a);color:#fff;font-family:'Unbounded',sans-serif}
.brand-title{color:#fff;font-size:1rem;font-weight:700;font-family:'Unbounded',sans-serif}
.brand-subtitle{font-size:.76rem;opacity:.65}
.meta{display:flex;align-items:center;gap:.8rem;font-size:.84rem;flex-wrap:wrap}
.meta span{opacity:.75}
#todayDate{color:#94a3b8;font-size:.82rem}
#liveClock{color:#7dd3fc;font-weight:700;font-size:.85rem;letter-spacing:.03em}
#userGreeting{color:#7dd3fc;font-weight:600;font-size:.83rem;display:none}
.lang-switcher{display:flex;gap:.2rem}
.lang-btn{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.15);color:#dbe3f0;border-radius:6px;padding:.22rem .55rem;cursor:pointer;font-size:.75rem;font-weight:600;transition:.15s}
.lang-btn.active{background:var(--primary);border-color:var(--primary);color:#fff}


.main-nav{background:rgba(255,255,255,.96);backdrop-filter:blur(8px);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:10}
.nav-inner{display:flex;flex-wrap:wrap;gap:.4rem;padding:.65rem 0}
.nav-btn{border:1px solid var(--border);background:#fff;padding:.48rem .9rem;border-radius:10px;cursor:pointer;font-weight:600;font-size:.84rem;color:#2d3748;transition:.18s;font-family:'Nunito',sans-serif;white-space:nowrap}
.nav-btn:hover{border-color:var(--primary);color:var(--primary)}
.nav-btn.active{color:var(--primary);border-color:rgba(31,111,235,.4);background:rgba(31,111,235,.08)}


.btn{border:1px solid transparent;border-radius:10px;padding:.52rem 1.1rem;font-weight:600;cursor:pointer;font-family:'Nunito',sans-serif;font-size:.88rem;transition:.17s}
.btn.primary{color:#fff;background:var(--primary)}
.btn.primary:hover{background:var(--primary-dark);transform:translateY(-1px)}
.btn.ghost{border-color:var(--border);background:#fff;color:#334155}
.btn.ghost:hover{border-color:var(--primary);color:var(--primary)}
.btn.danger{color:#fff;background:var(--danger)}
.btn.accent{color:#fff;background:var(--accent)}
.btn.accent:hover{background:#0b7a5f}
.btn.warn{color:#fff;background:var(--warn)}
.btn.violet{color:#fff;background:var(--violet)}
.btn.violet:hover{background:var(--violet-dark)}
.btn.full{width:100%}
.btn.sm{padding:.35rem .75rem;font-size:.8rem}


.page{padding:1.4rem 0 3rem}
.tab-content{display:none}
.tab-content.active{display:block}
.card{background:var(--surface);border:1px solid var(--border);border-radius:16px;box-shadow:var(--shadow);padding:1.2rem 1.4rem;margin-bottom:1.2rem}
.card h2{font-family:'Unbounded',sans-serif;font-size:1rem;font-weight:600}
.section-head{display:flex;justify-content:space-between;align-items:center;gap:.8rem;margin-bottom:.5rem}
.hero{margin-bottom:1.2rem}
.hero h1{font-family:'Unbounded',sans-serif;font-size:clamp(1.15rem,2.5vw,1.75rem);font-weight:700;margin-bottom:.4rem}
.hero p{color:var(--muted);font-size:.93rem}


.filter-grid{margin-top:.8rem;display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:.7rem;align-items:end}
label{display:grid;gap:.3rem;font-weight:600;font-size:.86rem}
select,input[type=text],input[type=number],input[type=date],input[type=email],input[type=password],textarea{border:1px solid var(--border);border-radius:10px;padding:.52rem .7rem;font-size:.91rem;background:#fff;font-family:'Nunito',sans-serif;transition:border-color .15s;width:100%}
select:focus,input:focus,textarea:focus{outline:none;border-color:var(--primary)}
textarea{resize:vertical;min-height:80px}
.muted{color:var(--muted);font-size:.86rem}


.expensive-grid{margin-top:.9rem;display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:.8rem}
.expensive-card{border:1px solid #fde6a6;background:linear-gradient(145deg,#fffdf5,#fff9e8);border-radius:14px;padding:.9rem;transition:.18s}
.expensive-card:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(154,52,18,.1)}
.expensive-card h3{margin-bottom:.3rem;font-size:.95rem;font-weight:700}
.expensive-card p{font-size:.84rem;color:var(--muted);margin-bottom:.22rem}
.price{color:#9a3412!important;font-weight:700!important;font-size:.98rem!important}
.expensive-card .btn{margin-top:.6rem}


.table-wrap{margin-top:.8rem;overflow-x:auto}
table{border-collapse:collapse;width:100%;min-width:820px}
th,td{border-bottom:1px solid var(--border);padding:.6rem .7rem;text-align:left;vertical-align:middle;font-size:.88rem}
th{color:#334155;background:#f8fbff;font-weight:700;font-size:.79rem;text-transform:uppercase;letter-spacing:.04em}
tr:hover td{background:#f5f9ff}
.row-action{color:var(--accent);font-weight:700;cursor:pointer;padding:.28rem .6rem;border-radius:8px;border:1px solid rgba(15,157,122,.3);background:rgba(15,157,122,.07);font-size:.8rem;white-space:nowrap;display:inline-block;transition:.15s}
.row-action:hover{background:var(--accent);color:#fff}
.chat-action{color:var(--primary);font-weight:700;cursor:pointer;padding:.28rem .6rem;border-radius:8px;border:1px solid rgba(31,111,235,.3);background:rgba(31,111,235,.07);font-size:.8rem;white-space:nowrap;display:inline-block;transition:.15s;margin-left:.3rem}
.chat-action:hover{background:var(--primary);color:#fff}
.dist-action{color:var(--warn);font-weight:700;cursor:pointer;padding:.28rem .6rem;border-radius:8px;border:1px solid rgba(217,119,6,.3);background:rgba(217,119,6,.07);font-size:.8rem;white-space:nowrap;display:inline-block;transition:.15s;margin-left:.3rem}
.dist-action:hover{background:var(--warn);color:#fff}


.transport-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:1rem;margin-top:1rem}
.transport-card{border:1px solid var(--border);border-radius:14px;padding:1rem;background:#fff;transition:.18s;display:flex;gap:.9rem;align-items:flex-start}
.transport-card:hover{transform:translateY(-2px);box-shadow:var(--shadow)}
.tc-info{flex:1;min-width:0}
.tc-header{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:.5rem;flex-wrap:wrap;gap:.3rem}
.tc-type{font-size:.74rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;padding:.2rem .5rem;border-radius:6px;background:rgba(31,111,235,.1);color:var(--primary)}
.tc-driver{font-weight:700;font-size:.95rem;margin-bottom:.2rem}
.tc-meta{font-size:.82rem;color:var(--muted);line-height:1.8}
.tc-meta strong{color:var(--text)}
.tc-actions{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:.6rem}
.tc-badge{display:inline-block;font-size:.74rem;padding:.17rem .48rem;border-radius:6px;font-weight:600}
.badge-green{background:rgba(15,157,122,.12);color:#0b7a5f}
.badge-blue{background:rgba(31,111,235,.1);color:var(--primary)}
.badge-gold{background:rgba(217,119,6,.12);color:#92400e}
.badge-red{background:rgba(220,38,38,.1);color:var(--danger)}


.star-row{display:flex;gap:.3rem;margin:.4rem 0}
.star-btn{background:none;border:none;cursor:pointer;font-size:1.6rem;color:#94a3b8;transition:.1s;padding:0}
.star-btn:hover,.star-btn.active{color:#f59e0b}
.rating-display{display:inline-flex;align-items:center;gap:.25rem;font-size:.82rem;font-weight:700}
.rating-display .stars{color:#f59e0b;font-size:.9rem;letter-spacing:.02em}
.rating-display .val{color:var(--text)}


.form-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(215px,1fr));gap:.9rem;margin-top:1rem}
.form-full{grid-column:1/-1}
.form-actions{margin-top:1.2rem;display:flex;gap:.75rem;flex-wrap:wrap}
.form-title{font-family:'Unbounded',sans-serif;font-size:.98rem;font-weight:600;margin-bottom:.4rem}
.form-subtitle{color:var(--muted);font-size:.86rem;margin-bottom:.2rem}
.success-banner{background:rgba(15,157,122,.1);border:1px solid rgba(15,157,122,.35);border-radius:12px;padding:.9rem 1.1rem;color:#0b7a5f;font-weight:600;font-size:.88rem;display:none;align-items:center;gap:.6rem;margin-top:1rem}
.success-banner.show{display:flex}
.field-group-title{font-weight:700;font-size:.82rem;text-transform:uppercase;letter-spacing:.05em;color:var(--primary);margin:.8rem 0 .3rem;padding:.3rem .6rem;background:rgba(31,111,235,.06);border-radius:7px}


.broker-section{background:linear-gradient(135deg,rgba(124,58,237,.06),rgba(79,70,229,.06));border:1px solid rgba(124,58,237,.25);border-radius:14px;padding:1rem 1.2rem;margin-bottom:1rem}
.broker-section h3{font-size:.95rem;font-weight:700;color:#4f46e5;margin-bottom:.5rem}


.wallet-card{background:linear-gradient(135deg,#0f172a,#1e3a5f);color:#fff;border-radius:16px;padding:1.4rem;margin-bottom:1rem}
.wallet-balance{font-size:2rem;font-weight:800;font-family:'Unbounded',sans-serif;color:#7dd3fc;margin:.3rem 0 .1rem}
.wallet-sub{opacity:.65;font-size:.82rem}
.wallet-actions{display:flex;gap:.6rem;margin-top:.9rem;flex-wrap:wrap}
.wallet-frozen{color:#fbbf24;font-size:.88rem;margin-top:.3rem}
.tx-list{margin-top:.8rem;display:flex;flex-direction:column;gap:.5rem}
.tx-item{border:1px solid var(--border);border-radius:10px;padding:.65rem .9rem;display:flex;justify-content:space-between;align-items:center;font-size:.86rem;flex-wrap:wrap;gap:.4rem}
.tx-plus{color:var(--accent);font-weight:700}
.tx-minus{color:var(--danger);font-weight:700}
.tx-frozen{color:var(--warn);font-weight:700}


.chat-window{display:flex;flex-direction:column;height:450px;border:1px solid var(--border);border-radius:14px;overflow:hidden}
.chat-header{background:#f8fbff;border-bottom:1px solid var(--border);padding:.7rem 1rem;font-weight:700;font-size:.9rem;display:flex;justify-content:space-between;align-items:center}
.chat-messages{flex:1;overflow-y:auto;padding:.9rem;display:flex;flex-direction:column;gap:.6rem;background:#fafcff}
.chat-msg{max-width:70%;padding:.55rem .85rem;border-radius:12px;font-size:.86rem;line-height:1.5}
.chat-msg.mine{align-self:flex-end;background:var(--primary);color:#fff;border-bottom-right-radius:4px}
.chat-msg.other{align-self:flex-start;background:#fff;border:1px solid var(--border);border-bottom-left-radius:4px}
.chat-msg.system{align-self:center;max-width:85%;background:rgba(100,116,139,.09);border:1px solid rgba(100,116,139,.18);border-radius:20px;color:#475569;font-size:.78rem;font-style:italic;padding:.35rem .9rem;text-align:center}
.chat-msg.broker-msg{align-self:center;max-width:85%;background:rgba(124,58,237,.1);border:1px solid rgba(124,58,237,.25);border-radius:10px;color:#4f46e5;font-size:.82rem;padding:.45rem .9rem;text-align:center}
.chat-msg-meta{font-size:.71rem;opacity:.65;margin-top:.2rem}
.chat-input-row{border-top:1px solid var(--border);padding:.65rem .9rem;display:flex;gap:.6rem;background:#fff;align-items:center}
.chat-input-row input{flex:1;border:1px solid var(--border);border-radius:10px;padding:.45rem .7rem;font-size:.88rem;font-family:'Nunito',sans-serif}
.chat-input-row input:focus{outline:none;border-color:var(--primary)}


.my-loads-list{margin-top:1rem;display:flex;flex-direction:column;gap:.7rem}
.my-load-item{border:1px solid var(--border);border-radius:12px;padding:.75rem 1rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.5rem}
.my-load-info{font-size:.88rem;flex:1;min-width:0}
.my-load-info strong{display:block;font-size:.92rem}
.my-load-info span{color:var(--muted);font-size:.81rem}
.my-load-price{font-weight:700;color:#9a3412}
.my-load-actions{display:flex;gap:.4rem;flex-wrap:wrap;align-items:center}
.empty-state{text-align:center;padding:2.5rem 1rem;color:var(--muted)}
.empty-state .es-icon{font-size:2.5rem;margin-bottom:.7rem;opacity:.45}


.modal-overlay{position:fixed;inset:0;background:rgba(15,23,42,.65);backdrop-filter:blur(4px);z-index:100;display:none;align-items:center;justify-content:center;padding:1rem}
.modal-overlay.open{display:flex}
.modal{background:#fff;border-radius:20px;box-shadow:var(--shadow-lg);width:min(480px,100%);padding:1.8rem;position:relative;animation:modalIn .25s ease;max-height:90vh;overflow-y:auto}
.modal.wide{width:min(700px,100%)}
@keyframes modalIn{from{opacity:0;transform:scale(.95) translateY(10px)}}
.modal-close{position:absolute;top:1rem;right:1rem;background:none;border:none;cursor:pointer;font-size:1.3rem;color:var(--muted);line-height:1;transition:.15s}
.modal-close:hover{color:var(--text)}
.modal h2{font-family:'Unbounded',sans-serif;font-size:1.15rem;margin-bottom:.3rem}
.modal p.sub{color:var(--muted);font-size:.86rem;margin-bottom:1.3rem}
.auth-tabs{display:flex;gap:0;margin-bottom:1.3rem;border-bottom:2px solid var(--border)}
.auth-tab-btn{background:none;border:none;padding:.55rem 1.1rem;font-weight:700;font-size:.88rem;cursor:pointer;color:var(--muted);border-bottom:2px solid transparent;margin-bottom:-2px;transition:.15s;font-family:'Nunito',sans-serif}
.auth-tab-btn.active{color:var(--primary);border-bottom-color:var(--primary)}
.auth-form{display:none;flex-direction:column;gap:.8rem}
.auth-form.active{display:flex}
.auth-form label{font-weight:600;font-size:.86rem;display:grid;gap:.28rem}
.modal-footer{margin-top:.9rem;text-align:center;font-size:.81rem;color:var(--muted)}
.modal-footer a{color:var(--primary);cursor:pointer;font-weight:600;text-decoration:none}
.modal-footer a:hover{text-decoration:underline}
.auth-error{background:#fef2f2;border:1px solid #fecaca;border-radius:8px;padding:.5rem .8rem;color:var(--danger);font-size:.83rem;display:none}
.auth-error.show{display:block}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:.7rem}
.profile-badge{display:none;align-items:center;gap:.5rem;background:rgba(255,255,255,.1);border-radius:10px;padding:.3rem .7rem}
.profile-badge.show{display:flex}
.avatar{width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--accent));display:grid;place-items:center;font-weight:700;font-size:.77rem;color:#fff}


.dist-result{background:rgba(31,111,235,.06);border:1px solid rgba(31,111,235,.2);border-radius:10px;padding:.7rem 1rem;margin-top:.6rem;font-size:.88rem}
.dist-result strong{color:var(--primary);font-size:1rem}


.toast{position:fixed;right:18px;bottom:80px;background:#0f172a;color:#fff;border-radius:12px;padding:.72rem 1.1rem;opacity:0;transform:translateY(12px);pointer-events:none;transition:.22s ease;z-index:300;font-size:.86rem;font-weight:600;max-width:320px}
.toast.show{opacity:1;transform:translateY(0)}
.toast.success{background:var(--accent)}
.toast.error{background:var(--danger)}
.toast.warn{background:var(--warn)}

input.phone-input{letter-spacing:.04em}


.broker-request-card{border:1px solid var(--border);border-radius:12px;padding:.9rem 1rem;margin-bottom:.7rem;background:#fff}
.broker-request-card .req-route{font-weight:700;font-size:.95rem;margin-bottom:.25rem}
.broker-request-card .req-meta{font-size:.82rem;color:var(--muted);margin-bottom:.5rem}
.broker-actions{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:.5rem}
.broker-wallet-card{background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;border-radius:14px;padding:1.2rem;margin-bottom:1rem}
.broker-wallet-balance{font-size:1.8rem;font-weight:800;font-family:'Unbounded',sans-serif;color:#c4b5fd;margin:.3rem 0}
.broker-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:.7rem;margin-top:1rem}
.broker-stat{background:rgba(255,255,255,.12);border-radius:10px;padding:.7rem .9rem;text-align:center}
.broker-stat-num{font-size:1.4rem;font-weight:800;font-family:'Unbounded',sans-serif}
.broker-stat-label{font-size:.74rem;opacity:.8;margin-top:.1rem}


.broker-chat-grid{display:grid;grid-template-columns:minmax(240px,300px) 1fr;gap:1rem;align-items:start;margin-top:1rem}
.broker-chat-list{display:flex;flex-direction:column;gap:.45rem}
.broker-chat-item{border:1px solid var(--border);border-radius:10px;padding:.65rem .85rem;cursor:pointer;transition:.15s;background:#fff}
.broker-chat-item:hover,.broker-chat-item.active{border-color:rgba(124,58,237,.4);background:rgba(124,58,237,.05)}
.broker-chat-item strong{display:block;font-size:.88rem}
.broker-chat-item span{font-size:.78rem;color:var(--muted)}
.broker-chat-window{display:flex;flex-direction:column;height:420px;border:1px solid var(--border);border-radius:14px;overflow:hidden}
.broker-chat-header{background:linear-gradient(135deg,rgba(124,58,237,.08),rgba(79,70,229,.06));border-bottom:1px solid rgba(124,58,237,.2);padding:.65rem 1rem;font-weight:700;font-size:.88rem;display:flex;justify-content:space-between;align-items:center;color:#4f46e5}
.broker-chat-messages{flex:1;overflow-y:auto;padding:.9rem;display:flex;flex-direction:column;gap:.6rem;background:#fafcff}
.broker-chat-input{border-top:1px solid var(--border);padding:.55rem .9rem;display:flex;gap:.5rem;background:#fff}
.broker-chat-input input{flex:1;border:1px solid var(--border);border-radius:10px;padding:.4rem .65rem;font-size:.86rem;font-family:'Nunito',sans-serif}
.broker-chat-input input:focus{outline:none;border-color:#7c3aed}


.deal-card{border:1px solid var(--border);border-radius:12px;padding:.9rem 1rem;margin-bottom:.7rem;background:#fff;display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:.6rem}
.deal-info strong{display:block;font-size:.92rem;margin-bottom:.2rem}
.deal-info span{font-size:.82rem;color:var(--muted)}
.deal-actions{display:flex;gap:.4rem;flex-wrap:wrap}


.chat-suggestions{display:flex;flex-wrap:wrap;gap:.4rem;padding:.55rem .9rem;border-top:1px solid var(--border);background:#f8fbff}
.chat-suggestion{background:#fff;border:1px solid rgba(31,111,235,.35);color:var(--primary);border-radius:20px;padding:.28rem .75rem;font-size:.79rem;font-weight:600;cursor:pointer;transition:.15s;font-family:'Nunito',sans-serif}
.chat-suggestion:hover{background:var(--primary);color:#fff}
.chat-attach-btn{background:none;border:none;cursor:pointer;display:flex;align-items:center;transition:.15s;padding:.25rem;flex-shrink:0}
.chat-attach-btn:hover{opacity:.7}
.chat-attach-btn img{width:24px;height:24px;object-fit:contain}
.chat-input-wrapper{display:flex;flex-direction:column;border-top:1px solid var(--border);background:#fff}


.wallet-form{display:flex;flex-direction:column;gap:.85rem;margin-top:.5rem}
.wallet-grid-2{display:grid;grid-template-columns:1fr 1fr;gap:.7rem}
.wallet-panel{border:1px solid var(--border);border-radius:12px;padding:.8rem .9rem;background:#f8fbff}
.wallet-panel h4{font-size:.84rem;font-weight:800;margin-bottom:.45rem;color:#1e293b;text-transform:uppercase;letter-spacing:.04em}
.copy-row{display:flex;align-items:center;justify-content:space-between;gap:.5rem;border:1px dashed #c7d2e5;border-radius:10px;padding:.45rem .55rem;background:#fff;margin-bottom:.45rem;min-height:52px}
.copy-value{font-weight:800;font-size:.92rem;color:#0f172a;letter-spacing:.04em;font-family:Consolas,'Courier New',monospace;line-height:1.1}
.copy-btn{border:1px solid rgba(31,111,235,.3);background:rgba(31,111,235,.09);color:var(--primary);border-radius:8px;padding:.25rem .55rem;font-size:.76rem;font-weight:700;cursor:pointer}
.wallet-fee-note{font-size:.81rem;color:#1d4ed8;font-weight:700}
.wallet-recipient{font-size:.82rem;color:#334155;margin-bottom:.45rem}
.wallet-recipient strong{color:#0f172a}
.wallet-file-picker{display:grid;gap:.35rem}
.wallet-file-btn{display:inline-flex;align-items:center;justify-content:center;padding:.52rem .8rem;border-radius:10px;background:var(--primary);color:#fff;border:1px solid var(--primary);font-weight:700;font-size:.84rem;cursor:pointer;transition:.15s;width:fit-content}
.wallet-file-btn:hover{background:var(--primary-dark)}
.wallet-file-name{font-size:.8rem;color:#334155}

.support-float{position:fixed;bottom:22px;right:22px;z-index:200;display:flex;flex-direction:column;align-items:flex-end;gap:.5rem}
.support-float-btn{width:52px;height:52px;border-radius:50%;background:var(--violet);border:3px solid rgba(255,255,255,.9);box-shadow:0 6px 24px rgba(124,58,237,.45);display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.2s;position:relative}
.support-float-btn:hover{transform:scale(1.08);background:var(--violet-dark)}
.support-float-btn svg{width:22px;height:22px;fill:none;stroke:#fff;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.support-badge{position:absolute;top:-5px;right:-5px;background:#dc2626;color:#fff;font-size:.62rem;font-weight:800;width:18px;height:18px;border-radius:50%;display:none;align-items:center;justify-content:center;border:2px solid #fff;font-family:'Nunito',sans-serif}
.support-badge.show{display:flex}


.support-panel{position:fixed;bottom:82px;right:22px;z-index:199;width:360px;background:#fff;border-radius:18px;box-shadow:0 20px 60px rgba(15,23,42,.22);border:1px solid var(--border);overflow:hidden;display:none;flex-direction:column;animation:modalIn .2s ease;max-height:580px}
.support-panel.open{display:flex}
.support-panel-header{background:linear-gradient(135deg,var(--violet),#4f46e5);padding:.9rem 1rem;color:#fff;display:flex;justify-content:space-between;align-items:center}
.support-panel-header h3{font-family:'Unbounded',sans-serif;font-size:.85rem;font-weight:600}
.support-tabs-row{display:flex;border-bottom:1px solid var(--border);background:#f8fbff}
.support-tab{flex:1;background:none;border:none;padding:.6rem;font-size:.82rem;font-weight:700;cursor:pointer;color:var(--muted);border-bottom:2px solid transparent;margin-bottom:-1px;font-family:'Nunito',sans-serif;transition:.15s}
.support-tab.active{color:var(--violet);border-bottom-color:var(--violet)}
.support-guide-list{flex:1;overflow-y:auto;padding:.6rem}
.guide-article{border:1px solid var(--border);border-radius:10px;margin-bottom:.5rem;overflow:hidden}
.guide-article-header{padding:.6rem .8rem;cursor:pointer;font-weight:700;font-size:.84rem;display:flex;justify-content:space-between;align-items:center;background:#fafcff;transition:.15s}
.guide-article-header:hover{background:#f0f4fb}
.guide-article-body{padding:.7rem .85rem;font-size:.82rem;line-height:1.6;color:#334155;display:none;border-top:1px solid var(--border)}
.guide-article-body.open{display:block}
.support-chat-wrap{flex:1;display:flex;flex-direction:column;overflow:hidden}
.support-chat-msgs{flex:1;overflow-y:auto;padding:.7rem;display:flex;flex-direction:column;gap:.5rem;background:#fafcff}
.support-chat-empty{text-align:center;padding:1.5rem .5rem;color:var(--muted);font-size:.84rem}
.support-chat-empty .sce-icon{font-size:2rem;margin-bottom:.4rem;opacity:.4}
.support-chat-input-row{border-top:1px solid var(--border);padding:.5rem .65rem;display:flex;gap:.4rem;align-items:center;background:#fff}
.support-chat-input-row input{flex:1;border:1px solid var(--border);border-radius:10px;padding:.4rem .6rem;font-size:.83rem;font-family:'Nunito',sans-serif}
.support-chat-input-row input:focus{outline:none;border-color:var(--violet)}
.support-chat-send{background:var(--violet);color:#fff;border:none;border-radius:8px;padding:.4rem .7rem;font-size:.78rem;font-weight:700;cursor:pointer;font-family:'Nunito',sans-serif;white-space:nowrap}
.supmsg{max-width:80%;padding:.45rem .7rem;border-radius:10px;font-size:.82rem;line-height:1.5}
.supmsg.mine{align-self:flex-end;background:var(--violet);color:#fff;border-bottom-right-radius:3px}
.supmsg.reply{align-self:flex-start;background:#fff;border:1px solid var(--border);border-bottom-left-radius:3px}
.supmsg-meta{font-size:.69rem;opacity:.65;margin-top:.15rem}


.profile-verify-badge{display:inline-flex;align-items:center;gap:.35rem;border-radius:8px;padding:.25rem .6rem;font-size:.78rem;font-weight:700}
.pv-pending{background:rgba(217,119,6,.12);color:#92400e}
.pv-approved{background:rgba(15,157,122,.12);color:#0b7a5f}
.pv-none{background:rgba(100,116,139,.1);color:#475569}


.admin-card{background:linear-gradient(135deg,#0f172a,#1e1b4b);color:#fff;border-radius:16px;padding:1.4rem;margin-bottom:1rem}
.admin-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:.7rem;margin-top:.8rem}
.admin-stat{background:rgba(255,255,255,.1);border-radius:10px;padding:.7rem .9rem;text-align:center}
.admin-stat-num{font-size:1.5rem;font-weight:800;font-family:'Unbounded',sans-serif;color:#a5b4fc}
.admin-stat-label{font-size:.74rem;opacity:.75;margin-top:.1rem}
.admin-user-card{border:1px solid var(--border);border-radius:12px;padding:.9rem 1rem;margin-bottom:.65rem;background:#fff}
.admin-user-card.danger-user{border-color:rgba(220,38,38,.3);background:rgba(220,38,38,.03)}
.admin-user-card.warn-user{border-color:rgba(217,119,6,.3);background:rgba(217,119,6,.03)}
.warn-pips{display:inline-flex;gap:.2rem;margin-left:.4rem}
.warn-pip{width:10px;height:10px;border-radius:50%;background:#e5e7eb}
.warn-pip.filled{background:#dc2626}
.admin-notif{background:rgba(220,38,38,.08);border:1px solid rgba(220,38,38,.25);border-radius:10px;padding:.65rem .9rem;margin-bottom:.5rem;font-size:.84rem}


.rating-modal-stars{display:flex;gap:.4rem;margin:.5rem 0 .3rem}
.rating-modal-stars .star-btn{font-size:2rem}
.review-card{border:1px solid var(--border);border-radius:10px;padding:.65rem .9rem;margin-bottom:.5rem;font-size:.84rem}
.review-card .rev-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:.3rem;font-weight:700}

@media(max-width:640px){
  .meta{flex-direction:column;align-items:flex-end;gap:.3rem}
  .form-row{grid-template-columns:1fr}
  .transport-card{flex-direction:column}
  .wallet-grid-2{grid-template-columns:1fr}
  .broker-chat-grid{grid-template-columns:1fr}
  .support-panel{width:calc(100vw - 32px);right:16px}
}
</style>
</head>
<body>

<header class="topbar">
  <div class="container topbar-inner">
    <div class="brand">
      <span class="brand-logo">N</span>
      <div>
        <p class="brand-title">Nurtay</p>
        <p class="brand-subtitle" data-i18n="brand_sub">Биржа автоперевозок Казахстан</p>
      </div>
    </div>
    <div class="meta">
      <span id="todayDate"></span>
      <span id="liveClock"></span>
      <span id="userGreeting"></span>
      <div class="lang-switcher">
        <button class="lang-btn active" onclick="setLang('ru')">RU</button>
        <button class="lang-btn" onclick="setLang('kk')">ҚАЗ</button>
        <button class="lang-btn" onclick="setLang('en')">EN</button>
      </div>
      <div class="profile-badge" id="profileBadge">
        <div class="avatar" id="avatarLetter"></div>
        <span style="color:#e2e8f0;font-size:.84rem;font-weight:600" id="profileName"></span>
        <button class="btn ghost sm" id="logoutBtn" style="padding:.22rem .55rem;font-size:.76rem;">Выйти</button>
      </div>
      <button class="btn ghost" id="authBtn" style="font-size:.83rem;">Вход / Регистрация</button>
    </div>
  </div>
</header>

<nav class="main-nav">
  <div class="container nav-inner">
    <button class="nav-btn active" data-tab="loads">Поиск грузов</button>
    <button class="nav-btn" data-tab="transport">Поиск транспорта</button>
    <button class="nav-btn" data-tab="add-load">Добавить груз</button>
    <button class="nav-btn" data-tab="add-transport">Добавить транспорт</button>
    <button class="nav-btn" data-tab="wallet">Кошелёк</button>
    <button class="nav-btn" data-tab="chat-tab">Чат</button>
    <button class="nav-btn" data-tab="profile">Личный кабинет</button>
    <button class="nav-btn" id="brokerNavBtn" data-tab="broker" style="display:none!important;background:rgba(124,58,237,.08);color:#4f46e5;border-color:rgba(124,58,237,.3)">Панель брокера</button>
    <button class="nav-btn" id="adminNavBtn" data-tab="admin" style="display:none!important;background:rgba(124,58,237,.08);color:#4f46e5;border-color:rgba(124,58,237,.3)">Администрирование</button>
  </div>
</nav>

<main class="container page">

<!-- ═══ LOADS ═══ -->
<div class="tab-content active" id="tab-loads">
  <section class="hero">
    <h1>Грузы для перевозки по Казахстану</h1>
    <p>Надёжная биржа грузоперевозок — прямые сделки с гарантией оплаты.</p>
  </section>
  <section class="card">
    <h2>Подбор рейса</h2>
    <div class="filter-grid">
      <label>Откуда<select id="fromCity"></select></label>
      <label>Куда<select id="toCity"></select></label>
      <label>Тип кузова<select id="bodyType"><option value="all">Любой</option></select></label>
      <label>Вес, т<select id="weightFilter">
        <option value="all">Любой</option>
        <option value="1">до 1 т</option>
        <option value="3">до 3 т</option>
        <option value="5">до 5 т</option>
        <option value="10">до 10 т</option>
        <option value="15">до 15 т</option>
        <option value="20">до 20 т</option>
      </select></label>
      <label>Дата от<input type="date" id="dateFrom"></label>
      <label>Дата до<input type="date" id="dateTo"></label>
      <label>Тип оплаты<select id="payFilter">
        <option value="all">Любой</option>
        <option value="cash">Наличные</option>
        <option value="kaspi">Kaspi</option>
        <option value="halyk">Halyk Bank</option>
        <option value="freedom">Freedom Bank</option>
        <option value="jysan">Jysan Bank</option>
        <option value="bes">Bereke Bank</option>
      </select></label>
      <label>Мин. фрахт (тнг)<input type="number" id="minPriceFilter" min="0" placeholder="например 150000"></label>
      <button class="btn primary" id="findBtn">Найти грузы</button>
    </div>
    <p class="muted" id="resultsInfo" style="margin-top:.7rem;"></p>
  </section>
  <section class="card">
    <div class="section-head">
      <h2 id="topLoadsTitle">Топ выгодных грузов</h2>
      <button class="btn ghost sm" id="showAllExpensiveBtn">Показать все</button>
    </div>
    <div id="expensiveLoads" class="expensive-grid"></div>
  </section>
  <section class="card">
    <div class="section-head">
      <h2>Лента грузов</h2>
      <button class="btn ghost sm" id="resetFiltersBtn">Сбросить фильтры</button>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr>
          <th>Дата</th><th>Маршрут</th><th>Груз</th><th>Вес</th><th>Кузов</th><th>Оплата</th><th>Фрахт</th><th>Действие</th>
        </tr></thead>
        <tbody id="loadsTable"></tbody>
      </table>
    </div>
  </section>
</div>

<!-- ═══ TRANSPORT ═══ -->
<div class="tab-content" id="tab-transport">
  <section class="hero">
    <h1>Поиск транспорта</h1>
    <p>Найдите подходящее транспортное средство для вашего груза.</p>
  </section>
  <section class="card">
    <h2>Фильтр транспорта</h2>
    <div class="filter-grid">
      <label>Город<select id="tc-fromCity"></select></label>
      <label>Тип кузова<select id="tc-body"><option value="all">Любой</option></select></label>
      <label>Грузоподъёмность<select id="tc-cap">
        <option value="all">Любая</option>
        <option value="1">до 1 т</option>
        <option value="3">до 3 т</option>
        <option value="5">до 5 т</option>
        <option value="10">до 10 т</option>
        <option value="20">до 20 т</option>
      </select></label>
      <button class="btn primary" id="tc-findBtn">Найти транспорт</button>
    </div>
  </section>
  <section class="card">
    <div class="section-head">
      <h2>Доступный транспорт</h2>
      <span class="muted" id="tc-resultsInfo"></span>
    </div>
    <div id="transportList" class="transport-grid"></div>
  </section>
</div>

<!-- ═══ ADD LOAD ═══ -->
<div class="tab-content" id="tab-add-load">
  <section class="hero">
    <h1>Добавить груз</h1>
    <p>Разместите заявку — перевозчики свяжутся через защищённый чат.</p>
  </section>
  <section class="card">
    <p class="form-title">Новая заявка на перевозку</p>
    <div class="field-group-title">Маршрут</div>
    <div class="form-grid">
      <label>Откуда<select id="al-from"></select></label>
      <label>Куда<select id="al-to"></select></label>
      <label>Дата погрузки<input type="date" id="al-date"></label>
      <label>Наименование груза<input type="text" id="al-cargo" placeholder="Металл, Продукты, Оборудование..."></label>
      <label>Вес (т)<input type="number" id="al-weight" placeholder="10" min="0.1" step="0.1"></label>
      <label>Объём (м³)<input type="number" id="al-volume" placeholder="напр. 80" min="0.1" step="0.1"></label>
      <label>Тип кузова<select id="al-body"><option value="">— выберите —</option></select></label>
      <label>Способ погрузки<select id="al-loading">
        <option value="верхняя">Верхняя</option>
        <option value="боковая">Боковая</option>
        <option value="задняя">Задняя</option>
        <option value="боковая/задняя">Боковая + Задняя</option>
        <option value="любая">Любая</option>
      </select></label>
      <label>Фрахт (тнг)<input type="number" id="al-price" placeholder="250000" min="0"></label>
      <label>Тип оплаты<select id="al-pay">
        <option value="cash">Наличные</option>
        <option value="kaspi">Kaspi</option>
        <option value="halyk">Halyk Bank</option>
        <option value="freedom">Freedom Bank</option>
        <option value="jysan">Jysan Bank</option>
        <option value="bes">Bereke Bank</option>
      </select></label>
      <label>Температурный режим<select id="al-temp">
        <option value="">Не требуется</option>
        <option value="+2/+6">+2/+6 °C (Охлаждение)</option>
        <option value="-18">-18 °C (Заморозка)</option>
        <option value="-25">-25 °C (Глубокая заморозка)</option>
        <option value="heated">Отапливаемый</option>
      </select></label>
      <label>Контактный телефон<input type="text" id="al-phone" class="phone-input" placeholder="+7 (___) ___ __ __"></label>
      <label>Компания / ИП / ТОО<input type="text" id="al-company" placeholder="Например: ТОО Астана Логистик"></label>
      <div class="form-full">
        <label>Дополнительно<textarea id="al-notes" placeholder="Особые условия, опасный груз, страхование..."></textarea></label>
      </div>
    </div>
    <div class="form-actions">
      <button class="btn primary" id="al-submitBtn">Разместить груз</button>
      <button class="btn ghost" id="al-resetBtn">Очистить</button>
    </div>
    <div class="success-banner" id="al-success">Груз успешно размещён! Перевозчики увидят вашу заявку.</div>
  </section>
</div>

<!-- ═══ ADD TRANSPORT ═══ -->
<div class="tab-content" id="tab-add-transport">
  <section class="hero">
    <h1>Добавить транспорт</h1>
    <p>Зарегистрируйте ТС и получайте заказы напрямую.</p>
  </section>
  <section class="card">
    <p class="form-title">Регистрация транспортного средства</p>
    <div class="field-group-title">Водитель</div>
    <div class="form-grid">
      <label>ФИО водителя<input type="text" id="at-name" placeholder="Иванов Иван Иванович"></label>
      <label>Телефон<input type="text" id="at-phone" class="phone-input" placeholder="+7 (___) ___ __ __"></label>
    </div>
    <div class="field-group-title">Транспортное средство</div>
    <div class="form-grid">
      <label>Марка/модель<input type="text" id="at-model" placeholder="Volvo FH16, MAN TGX..."></label>
      <label>Тип кузова<select id="at-body"><option value="">— выберите —</option></select></label>
      <label>Грузоподъёмность (т)<input type="number" id="at-cap" placeholder="20" min="0.5"></label>
      <label>Объём кузова (м³)<input type="number" id="at-volume" placeholder="86" min="1"></label>
      <label>Год выпуска<input type="number" id="at-year" placeholder="2020" min="1990" max="2026"></label>
      <label>Гос. номер<input type="text" id="at-plates" placeholder="123 ABC 01"></label>
      <label>Базовый город<input type="text" id="at-city" placeholder="Астана"></label>
      <label>Маршруты<input type="text" id="at-routes" placeholder="Астана – Алматы – Шымкент"></label>
      <label>Свободен с<input type="date" id="at-free"></label>
    </div>
    <div class="form-actions">
      <button class="btn primary" id="at-submitBtn">Зарегистрировать транспорт</button>
      <button class="btn ghost" id="at-resetBtn">Очистить</button>
    </div>
    <div class="success-banner" id="at-success">Транспорт добавлен в поиск!</div>
  </section>
</div>

<!-- ═══ WALLET ═══ -->
<div class="tab-content" id="tab-wallet">
  <section class="hero">
    <h1>Кошелёк</h1>
    <p>Безопасные расчёты с эскроу-защитой.</p>
  </section>
  <div id="walletGuest" class="card" style="text-align:center;padding:2.5rem">
    <div style="font-size:2.5rem;margin-bottom:.8rem">🔐</div>
    <p style="font-weight:600;margin-bottom:.5rem">Требуется авторизация</p>
    <button class="btn primary" onclick="openAuth()">Войти для продолжения</button>
  </div>
  <div id="walletUser" style="display:none">
    <div class="wallet-card">
      <div class="wallet-sub">Баланс кошелька</div>
      <div class="wallet-balance" id="walletBalance">0 ₸</div>
      <div class="wallet-frozen" id="walletFrozen"></div>
      <div class="wallet-actions">
        <button class="btn primary sm" onclick="openWalletModal('deposit')">Пополнить</button>
        <button class="btn sm" style="color:#fff;background:rgba(15,23,42,.45);border-color:rgba(255,255,255,.3)" onclick="openWalletModal('withdraw')">Вывести</button>
      </div>
    </div>
    <div class="card">
      <div class="section-head"><h2>История транзакций</h2></div>
      <div id="txList" class="tx-list"></div>
    </div>
    <div class="broker-section">
      <h3>Посреднические услуги</h3>
      <p style="font-size:.86rem;color:var(--muted)">При использовании посредника (брокера) комиссия 1% удерживается с обеих сторон сделки.</p>
      <div style="margin-top:.7rem;font-size:.84rem">Назначенный брокер: <strong id="brokerNameDisplay" style="color:#4f46e5">Гульназ Нуртай</strong></div>
    </div>
  </div>
</div>

<!-- ═══ CHAT ═══ -->
<div class="tab-content" id="tab-chat-tab">
  <section class="hero">
    <h1>Чат</h1>
    <p>Общайтесь с контрагентами по грузам и транспорту.</p>
  </section>
  <div id="chatGuest" class="card" style="text-align:center;padding:2.5rem">
    <div style="font-size:2.5rem;margin-bottom:.8rem">💬</div>
    <p style="font-weight:600;margin-bottom:.5rem">Требуется авторизация</p>
    <button class="btn primary" onclick="openAuth()">Войти для продолжения</button>
  </div>
  <div id="chatUser" style="display:none">
    <div style="display:grid;grid-template-columns:minmax(280px,340px) 1fr;gap:1rem;align-items:start">
      <section class="card" style="position:sticky;top:82px">
        <h2>Мои чаты</h2>
        <div id="chatList" style="margin-top:.8rem;display:flex;flex-direction:column;gap:.5rem"></div>
      </section>
      <section class="card">
        <div class="section-head">
          <h2 id="chatTitle">Чат по заказу</h2>
        </div>
        <div class="chat-window">
          <div class="chat-header">
            <span id="chatRouteLabel">Маршрут не выбран</span>
            <span id="chatOrderStatus" class="tc-badge badge-blue">Активен</span>
          </div>
          <div class="chat-messages" id="chatMessages"></div>
          <div class="chat-input-row">
            <button class="chat-attach-btn" title="Прикрепить файл" onclick="document.getElementById('mainChatFileInput').click()">
              <img src="https://9fc9bef3-40e0-44ee-8777-7ce6ada99b7e.selcdn.net/i/webp/48/9dd602135479c8ad2e7056efe1b2e1.webp" width="24" height="24" alt="attach">
            </button>
            <input type="file" id="mainChatFileInput" style="display:none" onchange="attachMainChatFile(this)">
            <input type="text" id="chatInput" placeholder="Введите сообщение..." onkeydown="if(event.key==='Enter')sendChatMsg()">
            <button class="btn primary sm" onclick="sendChatMsg()">Отправить</button>
          </div>
        </div>
        <div style="margin-top:.8rem;display:flex;gap:.6rem;flex-wrap:wrap">
          <button class="btn accent sm" id="confirmDeliveryBtn" onclick="confirmDelivery()">Подтвердить доставку (водитель)</button>
          <button class="btn primary sm" id="confirmReceiptBtn" onclick="confirmReceipt()">Получил заказ (компания)</button>
        </div>
      </section>
    </div>
  </div>
</div>

<!-- ═══ PROFILE ═══ -->
<div class="tab-content" id="tab-profile">
  <section class="hero">
    <h1>Личный кабинет</h1>
    <p id="profileSubtitle">Управляйте грузами, транспортом и сделками.</p>
  </section>
  <div id="profileGuest" class="card" style="text-align:center;padding:2.5rem">
    <div style="font-size:2.5rem;margin-bottom:.8rem">🔐</div>
    <p style="font-weight:600;margin-bottom:.5rem">Вы не авторизованы</p>
    <button class="btn primary" id="profileAuthBtn">Войти / Зарегистрироваться</button>
  </div>
  <div id="profileUser" style="display:none">
    <div class="card">
      <div style="display:flex;align-items:center;gap:1.2rem;flex-wrap:wrap">
        <div id="bigAvatar" style="width:60px;height:60px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--accent));display:grid;place-items:center;font-size:1.4rem;font-weight:700;color:#fff"></div>
        <div style="flex:1">
          <p style="font-size:1.05rem;font-weight:700" id="profileFullName"></p>
          <p class="muted" style="font-size:.86rem" id="profileEmail"></p>
          <p style="font-size:.82rem;margin-top:.2rem" id="profileRoleBadge"></p>
          <p style="font-size:.82rem;margin-top:.3rem" id="profileCompanyDisplay"></p>
          <div id="profileVerifyBadge" style="margin-top:.35rem"></div>
          <div id="profileRatingDisplay" style="margin-top:.35rem"></div>
        </div>
        <div style="display:flex;flex-direction:column;gap:.4rem;align-items:flex-end">
          <span class="tc-badge badge-green">Активный аккаунт</span>
          <button class="btn primary sm" onclick="openProfileEdit()">✏️ Изменить профиль</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="section-head">
        <h2>Мои грузы</h2>
        <button class="btn ghost sm" onclick="switchTab('add-load')">+ Добавить</button>
      </div>
      <div id="myLoadsList" class="my-loads-list"></div>
    </div>
    <div class="card">
      <div class="section-head">
        <h2>Мой транспорт</h2>
        <button class="btn ghost sm" onclick="switchTab('add-transport')">+ Добавить</button>
      </div>
      <div id="myTransportList" class="my-loads-list"></div>
    </div>
    <div class="card" id="myReviewsCard" style="display:none">
      <div class="section-head"><h2>Мои отзывы</h2></div>
      <div id="myReviewsList" style="margin-top:.7rem"></div>
    </div>
  </div>
</div>

<!-- ═══ BROKER PANEL ═══ -->
<div class="tab-content" id="tab-broker">
  <section class="hero">
    <h1 style="font-family:'Unbounded',sans-serif">Панель брокера</h1>
    <p>Управление сделками, контактами и комиссиями — Гульназ Нуртай</p>
  </section>
  <div id="brokerPanelGuest" class="card" style="text-align:center;padding:2.5rem">
    <div style="font-size:2.5rem;margin-bottom:.8rem">🔐</div>
    <p style="font-weight:700;margin-bottom:.4rem">Доступ только для брокера</p>
    <div style="max-width:340px;margin:0 auto;display:flex;flex-direction:column;gap:.7rem">
      <input type="text" id="brokerLoginInput" placeholder="Телефон посредника" style="text-align:center">
      <input type="password" id="brokerPwdInput" placeholder="Пароль посредника" style="text-align:center">
      <button class="btn primary" onclick="brokerLogin()">Войти как посредник</button>
      <div id="brokerLoginError" class="auth-error" style="display:none;text-align:center">Неверные данные.</div>
    </div>
  </div>
  <div id="brokerPanelUser" style="display:none">
    <div class="broker-wallet-card">
      <div style="font-size:.82rem;opacity:.75;margin-bottom:.2rem">Кошелёк брокера — Гульназ Нуртай</div>
      <div class="broker-wallet-balance" id="brokerWalletBalance">0 ₸</div>
      <div style="font-size:.82rem;opacity:.7">Комиссия 1% от каждой стороны сделки</div>
      <div class="broker-stats">
        <div class="broker-stat"><div class="broker-stat-num" id="brokerDealsCount">0</div><div class="broker-stat-label">Сделок завершено</div></div>
        <div class="broker-stat"><div class="broker-stat-num" id="brokerPendingCount">0</div><div class="broker-stat-label">Ожидают одобрения</div></div>
        <div class="broker-stat"><div class="broker-stat-num" id="brokerEarnedTotal">0 ₸</div><div class="broker-stat-label">Заработано всего</div></div>
      </div>
    </div>
    <div class="card">
      <div class="section-head">
        <h2>Сообщения в поддержку</h2>
        <span class="muted" id="brokerSupportCount" style="font-size:.82rem"></span>
      </div>
      <div id="brokerSupportList" style="margin-top:.7rem"></div>
    </div>
    <div class="card">
      <div class="section-head"><h2>Запросы на контакты</h2></div>
      <div id="brokerContactRequests" style="margin-top:.8rem"></div>
    </div>
    <div class="card">
      <div class="section-head"><h2>История пополнений (на одобрении)</h2></div>
      <div id="brokerDepositsList" style="margin-top:.8rem"></div>
    </div>
    <div class="card">
      <div class="section-head"><h2>История выводов (на одобрении)</h2></div>
      <div id="brokerWithdrawalsList" style="margin-top:.8rem"></div>
    </div>
    <div class="card">
      <div class="section-head">
        <h2>Активные сделки</h2>
        <button class="btn ghost sm" onclick="renderBrokerPanel()">Обновить</button>
      </div>
      <div id="brokerDealsList" style="margin-top:.8rem"></div>
    </div>
    <div class="card">
      <div class="section-head">
        <h2>Активные чаты</h2>
        <span class="muted" style="font-size:.82rem">Все переписки пользователей</span>
      </div>
      <div class="broker-chat-grid">
        <div>
          <div class="broker-chat-list" id="brokerChatList"></div>
        </div>
        <div>
          <div class="broker-chat-window" id="brokerChatWindow">
            <div class="broker-chat-header">
              <span id="brokerActiveChatLabel">Выберите чат слева</span>
              <span class="tc-badge badge-blue" id="brokerActiveChatStatus">Активен</span>
            </div>
            <div class="broker-chat-messages" id="brokerChatMessages">
              <div style="text-align:center;color:var(--muted);padding:2rem;font-size:.86rem">Выберите чат из списка слева</div>
            </div>
            <div class="broker-chat-input">
              <input type="text" id="brokerChatInput" placeholder="Напишите от имени брокера..." onkeydown="if(event.key==='Enter')sendBrokerChatMsg()">
              <button class="btn sm" style="background:#4f46e5;color:#fff;border-color:#4f46e5" onclick="sendBrokerChatMsg()">Отправить</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="section-head"><h2>История транзакций</h2></div>
      <div id="brokerTxList" style="margin-top:.8rem"></div>
    </div>
  </div>
</div>

<!-- ═══ ADMIN PANEL ═══ -->
<div class="tab-content" id="tab-admin">
  <section class="hero">
    <h1 style="font-family:'Unbounded',sans-serif">Администрирование</h1>
    <p>Управление пользователями, рейтингами и предупреждениями.</p>
  </section>
  <div id="adminGuest" class="card" style="text-align:center;padding:2.5rem">
    <div style="font-size:2.5rem;margin-bottom:.8rem">🛡️</div>
    <p style="font-weight:700;margin-bottom:.4rem">Панель администратора</p>
    <p class="muted" style="font-size:.86rem;margin-bottom:1rem">Введите пароль администратора</p>
    <div style="max-width:340px;margin:0 auto;display:flex;flex-direction:column;gap:.7rem">
      <input type="password" id="adminPwdInput" placeholder="Пароль администратора" style="text-align:center">
      <button class="btn violet" onclick="adminLogin()">Войти</button>
      <div id="adminLoginError" class="auth-error" style="display:none;text-align:center">Неверный пароль.</div>
    </div>
  </div>
  <div id="adminPanelUser" style="display:none">
    <div class="admin-card">
      <div style="font-size:.82rem;opacity:.75;margin-bottom:.3rem">Панель администратора Nurtay</div>
      <div class="admin-stats">
        <div class="admin-stat"><div class="admin-stat-num" id="adminUsersCount">0</div><div class="admin-stat-label">Пользователей</div></div>
        <div class="admin-stat"><div class="admin-stat-num" id="adminFlaggedCount">0</div><div class="admin-stat-label">На контроле</div></div>
        <div class="admin-stat"><div class="admin-stat-num" id="adminWarnCount">0</div><div class="admin-stat-label">Предупреждений</div></div>
        <div class="admin-stat"><div class="admin-stat-num" id="adminDeletedCount">0</div><div class="admin-stat-label">Удалено</div></div>
      </div>
    </div>
    <div class="card">
      <div class="section-head">
        <h2>⚠️ Уведомления администратора</h2>
      </div>
      <div id="adminNotifList" style="margin-top:.7rem"></div>
    </div>
    <div class="card">
      <div class="section-head">
        <h2>Пользователи с низким рейтингом</h2>
        <span class="muted" style="font-size:.82rem">Рейтинг ≤ 2.5 или 3 предупреждения</span>
      </div>
      <div id="adminFlaggedList" style="margin-top:.7rem"></div>
    </div>
    <div class="card">
      <div class="section-head">
        <h2>Все пользователи</h2>
        <button class="btn ghost sm" onclick="renderAdminPanel()">Обновить</button>
      </div>
      <div id="adminAllUsers" style="margin-top:.7rem"></div>
    </div>
  </div>
</div>

</main>

<!-- ═══ FLOATING GUIDE/SUPPORT ═══ -->
<div class="support-float">
  <div class="support-float-btn" id="supportFloatBtn" onclick="toggleSupportPanel()" title="Гид и поддержка">
    <svg viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
    <div class="support-badge" id="supportBadge"></div>
  </div>
</div>

<div class="support-panel" id="supportPanel">
  <div class="support-panel-header">
    <h3>🟣 Гид & Поддержка Nurtay</h3>
    <button onclick="toggleSupportPanel()" style="background:none;border:none;color:rgba(255,255,255,.7);cursor:pointer;font-size:1.1rem;line-height:1">✕</button>
  </div>
  <div class="support-tabs-row">
    <button class="support-tab active" id="guideTab" onclick="switchSupportTab('guide')">📖 Гид</button>
    <button class="support-tab" id="supportChatTabBtn" onclick="switchSupportTab('support')">💬 Поддержка</button>
  </div>
  <div id="guidePanelContent" class="support-guide-list">
    <div class="guide-article">
      <div class="guide-article-header" onclick="toggleArticle(this)">🔍 Как найти груз <span>▾</span></div>
      <div class="guide-article-body">На вкладке <strong>«Поиск грузов»</strong> используйте фильтры: откуда, куда, тип кузова, вес, дату и способ оплаты. Нажмите <em>«Найти грузы»</em>. Кликните <em>«Откликнуться»</em> рядом с нужным грузом — откроется карта маршрута и чат с заказчиком.</div>
    </div>
    <div class="guide-article">
      <div class="guide-article-header" onclick="toggleArticle(this)">📦 Как разместить груз <span>▾</span></div>
      <div class="guide-article-body">Перейдите на вкладку <strong>«Добавить груз»</strong>. Заполните маршрут, тип кузова, вес, фрахт и контактный телефон. После публикации груз появится в ленте — водители смогут откликнуться.</div>
    </div>
    <div class="guide-article">
      <div class="guide-article-header" onclick="toggleArticle(this)">🚛 Как найти транспорт <span>▾</span></div>
      <div class="guide-article-body">Вкладка <strong>«Поиск транспорта»</strong>. Выберите город, тип кузова, грузоподъёмность. Нажмите кнопку водителя <em>«Перейти в чат»</em> или <em>«Заказать»</em> — откроется форма заказа.</div>
    </div>
    <div class="guide-article">
      <div class="guide-article-header" onclick="toggleArticle(this)">🚗 Как добавить транспорт <span>▾</span></div>
      <div class="guide-article-body">Вкладка <strong>«Добавить транспорт»</strong>. Укажите ФИО, телефон, марку авто, кузов, грузоподъёмность и базовый город. Транспорт появится в поиске для компаний.</div>
    </div>
    <div class="guide-article">
      <div class="guide-article-header" onclick="toggleArticle(this)">💳 Как пополнить кошелёк <span>▾</span></div>
      <div class="guide-article-body"><strong>Кошелёк → Пополнить</strong>. Выберите банк (Kaspi, Halyk и др.), введите сумму, переведите деньги по реквизитам <strong>Гульназ Нуртай</strong>, прикрепите скриншот чека. Комиссия 5%. Средства будут зачислены после проверки брокером.</div>
    </div>
    <div class="guide-article">
      <div class="guide-article-header" onclick="toggleArticle(this)">🛡️ Верификация профиля <span>▾</span></div>
      <div class="guide-article-body">Перейдите в <strong>Личный кабинет → Изменить профиль</strong>. Загрузите фото паспорта, удостоверения личности или водительских прав. Верификация подтверждает личность и повышает доверие контрагентов.</div>
    </div>
    <div class="guide-article">
      <div class="guide-article-header" onclick="toggleArticle(this)">🤝 Как оформить сделку <span>▾</span></div>
      <div class="guide-article-body">1. Откликнитесь на груз → откроется чат. 2. Обсудите условия. 3. Нажмите <em>«Подтвердить сделку»</em> — спишется 1% комиссии брокеру. 4. После доставки водитель нажимает <em>«Подтвердить доставку»</em>, компания — <em>«Получил заказ»</em>. 5. После взаимного подтверждения система разморозит средства.</div>
    </div>
    <div class="guide-article">
      <div class="guide-article-header" onclick="toggleArticle(this)">⭐ Система рейтингов <span>▾</span></div>
      <div class="guide-article-body">После завершения сделки система предложит поставить оценку (1–5 звёзд) водителю или компании. Средний рейтинг виден в карточках транспорта и профиле. Рейтинг ниже 2.5 ⭐ попадает на контроль администратора.</div>
    </div>
    <div class="guide-article">
      <div class="guide-article-header" onclick="toggleArticle(this)">🔒 Система посредника <span>▾</span></div>
      <div class="guide-article-body">Брокер Гульназ Нуртай контролирует все сделки. Комиссия — 1% с каждой стороны при подтверждении сделки. Брокер одобряет пополнения и выводы, а также раскрывает контакты по запросу.</div>
    </div>
  </div>
  <div id="supportChatContent" class="support-chat-wrap" style="display:none">
    <div class="support-chat-msgs" id="supportChatMsgs">
      <div class="support-chat-empty">
        <div class="sce-icon">💬</div>
        <p>Нет сообщений</p>
        <p style="font-size:.78rem;margin-top:.25rem">Тут будут отображаться вопросы / жалобы</p>
      </div>
    </div>
    <div style="border-top:1px solid var(--border);padding:.4rem .6rem .3rem;background:#f8fbff">
      <label style="display:flex;align-items:center;gap:.4rem;cursor:pointer;font-size:.78rem;color:var(--muted)">
        <input type="file" id="supportFileInput" style="display:none" onchange="attachSupportFile(this)">
        <button class="chat-attach-btn" onclick="document.getElementById('supportFileInput').click()" style="border:1px solid var(--border);border-radius:8px;padding:.2rem .4rem">
          <img src="https://9fc9bef3-40e0-44ee-8777-7ce6ada99b7e.selcdn.net/i/webp/48/9dd602135479c8ad2e7056efe1b2e1.webp" width="18" height="18" alt="attach">
        </button>
        Прикрепить файл
      </label>
    </div>
    <div class="support-chat-input-row">
      <input type="text" id="supportChatInput" placeholder="Напишите вопрос или жалобу..." onkeydown="if(event.key==='Enter')sendSupportMsg()">
      <button class="support-chat-send" onclick="sendSupportMsg()">Отправить</button>
    </div>
  </div>
</div>

<!-- CHAT MODAL -->
<div class="modal-overlay" id="chatModal">
  <div class="modal wide">
    <button class="modal-close" onclick="document.getElementById('chatModal').classList.remove('open')">&#x2715;</button>
    <h2 id="chatModalTitle">Чат с перевозчиком</h2>
    <p class="sub" id="chatModalSub" style="margin-bottom:.8rem"></p>
    <div class="chat-window" style="height:380px">
      <div class="chat-header">
        <span id="chatModalRoute">Маршрут не выбран</span>
        <span class="tc-badge badge-blue">Защищённый чат</span>
      </div>
      <div class="chat-messages" id="chatModalMessages"></div>
      <div class="chat-input-wrapper">
        <div class="chat-suggestions" id="chatModalSuggestions">
          <span class="chat-suggestion" onclick="useSuggestion(this)">Здравствуйте! Готов к перевозке.</span>
          <span class="chat-suggestion" onclick="useSuggestion(this)">Когда можно забрать груз?</span>
          <span class="chat-suggestion" onclick="useSuggestion(this)">Уточните адрес загрузки</span>
          <span class="chat-suggestion" onclick="useSuggestion(this)">Условия оплаты?</span>
          <span class="chat-suggestion" onclick="useSuggestion(this)">Готов выехать сегодня</span>
        </div>
        <div class="chat-input-row" style="border-top:none">
          <button class="chat-attach-btn" title="Прикрепить файл" onclick="document.getElementById('chatModalFileInput').click()">
            <img src="https://9fc9bef3-40e0-44ee-8777-7ce6ada99b7e.selcdn.net/i/webp/48/9dd602135479c8ad2e7056efe1b2e1.webp" width="24" height="24" alt="attach">
          </button>
          <input type="file" id="chatModalFileInput" style="display:none" onchange="attachModalChatFile(this)">
          <input type="text" id="chatModalInput" placeholder="Введите сообщение..." onkeydown="if(event.key==='Enter')sendModalChatMsg()">
          <button class="btn primary sm" onclick="sendModalChatMsg()">Отправить</button>
        </div>
      </div>
    </div>
    <div style="margin-top:.9rem;padding:.7rem 1rem;background:rgba(124,58,237,.07);border-radius:10px;border:1px solid rgba(124,58,237,.2);font-size:.82rem;color:#4f46e5">
      <strong>Система посредника:</strong> При подтверждении сделки обе стороны переводят по 1% на кошелёк посредника.
      <div style="margin-top:.6rem;display:flex;gap:.5rem;flex-wrap:wrap">
        <button class="btn sm" id="requestContactBtn" style="background:#4f46e5;color:#fff" onclick="requestBrokerContact()">Запросить контакты у посредника</button>
        <button class="btn accent sm" id="confirmDealBtn" onclick="confirmDealInChat()">✓ Подтвердить сделку (списать 1%)</button>
      </div>
    </div>
  </div>
</div>

<!-- AUTH MODAL -->
<div class="modal-overlay" id="authModal">
  <div class="modal">
    <button class="modal-close" id="authModalClose">&#x2715;</button>
    <h2>Добро пожаловать</h2>
    <p class="sub">Войдите или создайте аккаунт</p>
    <div class="auth-tabs">
      <button class="auth-tab-btn active" data-auth="login">Вход</button>
      <button class="auth-tab-btn" data-auth="register">Регистрация</button>
    </div>
    <div class="auth-form active" id="authFormLogin">
      <div class="auth-error" id="loginError">Неверный телефон или пароль</div>
      <label>Телефон<input type="text" id="loginPhone" class="phone-input" placeholder="+7 (___) ___ __ __"></label>
      <label>Пароль<input type="password" id="loginPwd" placeholder="Ваш пароль"></label>
      <button class="btn primary full" id="loginSubmitBtn">Войти</button>
      <div class="modal-footer">Нет аккаунта? <a id="toRegisterLink">Зарегистрироваться</a></div>
    </div>
    <div class="auth-form" id="authFormRegister">
      <div class="auth-error" id="registerError"></div>
      <div class="form-row">
        <label>Имя<input type="text" id="regName" placeholder="Иван"></label>
        <label>Фамилия<input type="text" id="regSurname" placeholder="Иванов"></label>
      </div>
      <label>Телефон<input type="text" id="regPhone" class="phone-input" placeholder="+7 (___) ___ __ __"></label>
      <label>Пароль<input type="password" id="regPwd" placeholder="Минимум 6 символов"></label>
      <label>Повторите пароль<input type="password" id="regPwd2" placeholder="Повторите пароль"></label>
      <label>Роль<select id="regRole">
        <option value="shipper">Грузоотправитель / Компания</option>
        <option value="carrier">Перевозчик / Водитель</option>
      </select></label>
      <button class="btn primary full" id="registerSubmitBtn">Зарегистрироваться</button>
      <div class="modal-footer">Уже есть аккаунт? <a id="toLoginLink">Войти</a></div>
    </div>
  </div>
</div>

<!-- PROFILE EDIT MODAL -->
<div class="modal-overlay" id="profileEditModal">
  <div class="modal wide">
    <button class="modal-close" onclick="document.getElementById('profileEditModal').classList.remove('open')">&#x2715;</button>
    <h2>Редактировать профиль</h2>
    <p class="sub">Обновите личные данные и пройдите верификацию</p>
    <div class="field-group-title">Личные данные</div>
    <div class="form-grid">
      <label>Имя<input type="text" id="editName" placeholder="Иван"></label>
      <label>Фамилия<input type="text" id="editSurname" placeholder="Иванов"></label>
      <label>Телефон<input type="text" id="editPhone" class="phone-input" placeholder="+7 (___) ___ __ __"></label>
      <label>Email<input type="email" id="editEmail" placeholder="example@mail.com"></label>
      <label id="editCompanyLabel">Название компании<input type="text" id="editCompany" placeholder="ТОО Астана Логистик"></label>
    </div>
    <div class="field-group-title" style="margin-top:1rem">Верификация личности</div>
    <div style="background:#f8fbff;border:1px solid var(--border);border-radius:12px;padding:.9rem;margin-top:.4rem">
      <p style="font-size:.86rem;color:var(--muted);margin-bottom:.7rem">Загрузите фото/скан документа для подтверждения личности</p>
      <div style="display:flex;gap:.7rem;flex-wrap:wrap;margin-bottom:.6rem">
        <label style="font-size:.82rem;cursor:pointer"><input type="radio" name="verifyDocType" value="passport" checked> Паспорт</label>
        <label style="font-size:.82rem;cursor:pointer"><input type="radio" name="verifyDocType" value="id"> Удостоверение личности</label>
        <label style="font-size:.82rem;cursor:pointer"><input type="radio" name="verifyDocType" value="license"> Водительские права</label>
      </div>
      <div class="wallet-file-picker">
        <label for="verifyDocFile" class="wallet-file-btn" style="background:var(--violet)">📄 Загрузить документ</label>
        <input type="file" id="verifyDocFile" accept=".jpg,.jpeg,.png,.pdf" style="display:none">
        <div id="verifyDocFileName" class="wallet-file-name">Файл не выбран</div>
      </div>
      <div id="currentVerifyStatus" style="margin-top:.6rem"></div>
    </div>
    <div class="form-actions">
      <button class="btn primary" onclick="saveProfileEdit()">💾 Сохранить</button>
      <button class="btn ghost" onclick="document.getElementById('profileEditModal').classList.remove('open')">Отмена</button>
    </div>
  </div>
</div>

<!-- RESPOND MODAL -->
<div class="modal-overlay" id="respondModal">
  <div class="modal">
    <button class="modal-close" id="respondModalClose">&#x2715;</button>
    <h2>Откликнуться на груз</h2>
    <p class="sub" id="respondInfo"></p>
    <div style="display:flex;flex-direction:column;gap:.8rem;margin-top:.5rem">
      <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Ваш телефон<input type="text" id="respondPhone" class="phone-input" placeholder="+7 (___) ___ __ __"></label>
      <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Ваш автомобиль<input type="text" id="respondCar" placeholder="Марка, госномер"></label>
      <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Комментарий<textarea id="respondComment" placeholder="Уточните условия, сроки..."></textarea></label>
      <button class="btn primary" id="respondSubmitBtn">Отправить заявку</button>
    </div>
  </div>
</div>

<!-- DISTANCE MODAL -->
<div class="modal-overlay" id="distModal">
  <div class="modal">
    <button class="modal-close" id="distModalClose">&#x2715;</button>
    <h2>Расчёт расстояния</h2>
    <p class="sub" id="distRouteLabel"></p>
    <div class="dist-result" id="distResult" style="display:none">
      Расстояние: <strong id="distKm"></strong> км &nbsp;|&nbsp; Примерное время: <strong id="distTime"></strong>
    </div>
    <p class="muted" style="margin-top:.6rem;font-size:.82rem">* Расстояния рассчитаны по основным дорогам Казахстана</p>
  </div>
</div>

<!-- WALLET MODAL -->
<div class="modal-overlay" id="walletModal">
  <div class="modal">
    <button class="modal-close" onclick="document.getElementById('walletModal').classList.remove('open')">&#x2715;</button>
    <h2 id="walletModalTitle">Пополнение</h2>
    <p class="sub" id="walletModalSub"></p>
    <div class="wallet-form">
      <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Сумма (тнг)
        <input type="number" id="walletAmount" placeholder="10000" min="1000">
      </label>
      <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Банк / Метод оплаты
        <select id="walletBank">
          <option value="kaspi">Kaspi Bank</option>
          <option value="halyk">Halyk Bank</option>
          <option value="freedom">Freedom Bank</option>
          <option value="jysan">Jysan Bank</option>
          <option value="bes">Bereke Bank</option>
          <option value="forte">Forte Bank</option>
          <option value="eurasian">Евразийский банк</option>
          <option value="atf">ATF Bank</option>
          <option value="centerc">Центркредит</option>
          <option value="nurdaulet">Нурдаулет банк</option>
        </select>
      </label>
      <div id="walletRequisites" class="wallet-panel">
        <h4>Реквизиты получателя</h4>
        <div class="wallet-recipient">Получатель: <strong>Гульназ Нуртай</strong></div>
        <div class="wallet-grid-2">
          <div class="copy-row">
            <div class="copy-value" id="walletReqPhone">+7 777 777 7777</div>
            <button type="button" class="copy-btn" onclick="copyWalletValue('walletReqPhone')">Копировать</button>
          </div>
          <div class="copy-row">
            <div class="copy-value" id="walletReqCard">7777 7777 7777 7777</div>
            <button type="button" class="copy-btn" onclick="copyWalletValue('walletReqCard')">Копировать</button>
          </div>
        </div>
        <div id="walletFeeText" class="wallet-fee-note">Комиссия за пополнение: 5%</div>
      </div>
      <div id="walletReceiptWrap" style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">
        <span>Прикрепить чек (обязательно)</span>
        <div class="wallet-file-picker">
          <label for="walletReceipt" class="wallet-file-btn">Прикрепить чек</label>
          <input type="file" id="walletReceipt" accept=".jpg,.jpeg,.png,.pdf" style="display:none">
          <div id="walletReceiptName" class="wallet-file-name">Файл не выбран</div>
        </div>
      </div>
      <div id="walletWithdrawDetails" class="wallet-panel" style="display:none">
        <h4>Данные для вывода</h4>
        <div class="wallet-grid-2">
          <label style="font-weight:600;font-size:.84rem;display:grid;gap:.25rem">Имя<input type="text" id="withdrawFirstName" placeholder="Имя"></label>
          <label style="font-weight:600;font-size:.84rem;display:grid;gap:.25rem">Фамилия<input type="text" id="withdrawLastName" placeholder="Фамилия"></label>
        </div>
        <div class="wallet-grid-2">
          <label style="font-weight:600;font-size:.84rem;display:grid;gap:.25rem">Телефон<input type="text" id="withdrawPhone" class="phone-input" placeholder="+7 (___) ___ __ __"></label>
          <label style="font-weight:600;font-size:.84rem;display:grid;gap:.25rem">Номер карты<input type="text" id="withdrawCard" placeholder="7777 7777 7777 7777"></label>
        </div>
      </div>
      <button class="btn primary full" id="walletConfirmBtn">Подтвердить</button>
    </div>
  </div>
</div>

<!-- LOAD OFFER MODAL -->
<div class="modal-overlay" id="loadOfferModal">
  <div class="modal wide">
    <button class="modal-close" onclick="document.getElementById('loadOfferModal').classList.remove('open')">&#x2715;</button>
    <h2>Отклик на груз</h2>
    <p class="sub" id="loadOfferSub"></p>
    <div class="wallet-panel">
      <h4>Карта маршрута</h4>
      <iframe id="loadOfferMap" title="map" style="width:100%;height:260px;border:1px solid var(--border);border-radius:10px" src=""></iframe>
    </div>
    <div id="loadOfferDetails" class="wallet-panel" style="margin-top:.75rem"></div>
    <div class="wallet-grid-2" style="margin-top:.75rem">
      <label style="font-weight:600;font-size:.84rem;display:grid;gap:.25rem">Ваши расходы (тнг)
        <input type="number" id="loadOfferCosts" min="0" placeholder="Например 70000" oninput="recalcLoadProfit()">
      </label>
      <label style="font-weight:600;font-size:.84rem;display:grid;gap:.25rem">Прибыль
        <input type="text" id="loadOfferProfit" readonly>
      </label>
    </div>
    <div style="margin-top:.8rem;display:flex;justify-content:flex-end;gap:.5rem">
      <button class="btn ghost" onclick="document.getElementById('loadOfferModal').classList.remove('open')">Закрыть</button>
      <button class="btn primary" onclick="respondFromMapModal()">Откликнуться — открыть чат</button>
    </div>
  </div>
</div>

<!-- TRANSPORT ORDER MODAL -->
<div class="modal-overlay" id="transportOrderModal">
  <div class="modal wide">
    <button class="modal-close" onclick="document.getElementById('transportOrderModal').classList.remove('open')">&#x2715;</button>
    <h2>Заказать транспорт</h2>
    <p class="sub">Заполните детали заказа</p>
    <div class="form-grid">
      <label>Маршрут откуда<input type="text" id="to-from" placeholder="Астана"></label>
      <label>Маршрут куда<input type="text" id="to-to" placeholder="Алматы"></label>
      <label>Дата подачи<input type="date" id="to-date"></label>
      <label>Желаемая цена (тнг)<input type="number" id="to-price" min="0"></label>
      <label>Контактный телефон<input type="text" id="to-phone" class="phone-input" placeholder="+7 (___) ___ __ __"></label>
      <label>Компания<input type="text" id="to-company" placeholder="ТОО ..."></label>
      <div class="form-full">
        <label>Описание заказа<textarea id="to-notes" placeholder="Адрес загрузки, условия, требования"></textarea></label>
      </div>
    </div>
    <div style="margin-top:.8rem;display:flex;justify-content:flex-end">
      <button class="btn accent" onclick="submitTransportOrder()">Отправить заказ водителю</button>
    </div>
    <hr style="border:none;border-top:2px solid var(--border);margin:1rem 0">
    <h3 style="font-size:.95rem">Или выбрать из ваших грузов</h3>
    <div id="transportExistingOffers" style="margin-top:.65rem;display:flex;flex-direction:column;gap:.5rem"></div>
  </div>
</div>

<!-- EDIT LOAD MODAL -->
<div class="modal-overlay" id="editLoadModal">
  <div class="modal">
    <button class="modal-close" onclick="document.getElementById('editLoadModal').classList.remove('open')">&#x2715;</button>
    <h2>Редактировать груз</h2>
    <input type="hidden" id="editLoadIdx">
    <div style="display:flex;flex-direction:column;gap:.8rem;margin-top:.3rem">
      <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Откуда<input type="text" id="editLoadFrom"></label>
      <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Куда<input type="text" id="editLoadTo"></label>
      <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Наименование груза<input type="text" id="editLoadCargo"></label>
      <div class="form-row">
        <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Вес (т)<input type="number" id="editLoadWeight" min="0.1" step="0.1"></label>
        <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Фрахт (тнг)<input type="number" id="editLoadPrice" min="0"></label>
      </div>
      <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Компания<input type="text" id="editLoadCompany"></label>
      <button class="btn primary full" onclick="saveEditLoad()">Сохранить изменения</button>
    </div>
  </div>
</div>

<!-- EDIT TRANSPORT MODAL -->
<div class="modal-overlay" id="editTransportModal">
  <div class="modal">
    <button class="modal-close" onclick="document.getElementById('editTransportModal').classList.remove('open')">&#x2715;</button>
    <h2>Редактировать транспорт</h2>
    <input type="hidden" id="editTransportIdx">
    <div style="display:flex;flex-direction:column;gap:.8rem;margin-top:.3rem">
      <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">ФИО водителя<input type="text" id="editTransportName"></label>
      <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Марка/модель<input type="text" id="editTransportModel"></label>
      <div class="form-row">
        <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Грузоподъёмность (т)<input type="number" id="editTransportCap" min="0.5"></label>
        <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Город<input type="text" id="editTransportCity"></label>
      </div>
      <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem">Маршруты<input type="text" id="editTransportRoutes"></label>
      <button class="btn primary full" onclick="saveEditTransport()">Сохранить изменения</button>
    </div>
  </div>
</div>

<!-- RATING MODAL -->
<div class="modal-overlay" id="ratingModal">
  <div class="modal">
    <button class="modal-close" onclick="document.getElementById('ratingModal').classList.remove('open')">&#x2715;</button>
    <h2>Оставить отзыв</h2>
    <p class="sub">Оцените сделку и оставьте комментарий</p>
    <p style="font-weight:700;font-size:.95rem;margin-bottom:.3rem">Получатель отзыва: <span id="ratingTargetName" style="color:var(--primary)"></span></p>
    <div class="rating-modal-stars" id="ratingStars"></div>
    <p id="ratingValLabel" style="font-size:.84rem;color:var(--muted);margin-bottom:.6rem">Нажмите на звезду для оценки</p>
    <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem;margin-bottom:.7rem">
      Комментарий
      <textarea id="ratingComment" placeholder="Опишите опыт работы..." style="min-height:70px"></textarea>
    </label>
    <label style="font-weight:600;font-size:.86rem;display:grid;gap:.28rem;margin-bottom:.9rem">
      Фото / Видео (необязательно)
      <div class="wallet-file-picker">
        <label for="ratingFile" class="wallet-file-btn" style="background:var(--muted)">📎 Прикрепить файл</label>
        <input type="file" id="ratingFile" accept=".jpg,.jpeg,.png,.mp4,.pdf" style="display:none">
        <div id="ratingFileName" class="wallet-file-name">Файл не выбран</div>
      </div>
    </label>
    <button class="btn primary full" onclick="submitRating()">⭐ Отправить отзыв</button>
  </div>
</div>

<div class="toast" id="toast"></div>

<script>

const DISTANCES = {
  "Алматы-Астана":1200,"Астана-Алматы":1200,"Алматы-Шымкент":680,"Шымкент-Алматы":680,
  "Астана-Шымкент":1750,"Шымкент-Астана":1750,"Алматы-Павлодар":1280,"Павлодар-Алматы":1280,
  "Астана-Павлодар":380,"Павлодар-Астана":380,"Астана-Петропавловск":280,"Петропавловск-Астана":280,
  "Астана-Кокшетау":260,"Кокшетау-Астана":260,"Астана-Костанай":550,"Костанай-Астана":550,
  "Алматы-Оскемен":1150,"Оскемен-Алматы":1150,"Алматы-Атырау":2400,"Атырау-Алматы":2400,
  "Алматы-Аральск":1800,"Аральск-Алматы":1800,"Алматы-Жезказган":1100,"Жезказган-Алматы":1100,
  "Астана-Жезказган":800,"Жезказган-Астана":800,"Астана-Атырау":1700,"Атырау-Астана":1700,
  "Шымкент-Тараз":160,"Тараз-Шымкент":160,"Шымкент-Жезказган":1300,"Жезказган-Шымкент":1300,
  "Павлодар-Балхаш":840,"Балхаш-Павлодар":840,"Кокшетау-Павлодар":400,"Павлодар-Кокшетау":400,
  "Кокшетау-Казалинск":900,"Казалинск-Кокшетау":900,"Костанай-Алматы":1650,"Алматы-Костанай":1650,
  "Астана-Аральск":1500,"Аральск-Астана":1500,"Атырау-Шымкент":2100,"Шымкент-Атырау":2100,
  "Шубарколь-Аральск":600,"Аральск-Шубарколь":600,"Новоишимское-Качиры":200,"Качиры-Новоишимское":200,
  "Астана-Астана":0,"Оскемен-Астана":1400,"Астана-Оскемен":1400,
};
function getDistance(from,to){
  return DISTANCES[`${from}-${to}`]||DISTANCES[`${to}-${from}`]||null;
}
const PAY_LABELS={cash:"Наличные",card:"Карта",kaspi:"Kaspi",halyk:"Halyk",freedom:"Freedom",jysan:"Jysan",bes:"Bereke",transfer:"Безнал"};


const loads=[
  {date:"05.05",from:"Шымкент",to:"Алматы",cargo:"Автомобиль",weight:"2 т",body:"автовоз",price:450000,pay:"kaspi"},
  {date:"05.05",from:"Павлодар",to:"Аральск",cargo:"Рыба глубокой заморозки",weight:"1 т",body:"рефрижератор",price:260000,pay:"halyk"},
  {date:"05.05",from:"Кокшетау",to:"Казалинск",cargo:"Масло в бочках",weight:"10 т",body:"тент",price:450000,pay:"kaspi"},
  {date:"05.05",from:"Костанай",to:"Алматы",cargo:"Отходы синтепона",weight:"4.5 т",body:"тент",price:320000,pay:"cash"},
  {date:"05.05",from:"Новоишимское",to:"Качиры",cargo:"Агропродукция",weight:"20 т",body:"зерновоз",price:400000,pay:"kaspi"},
  {date:"05.05",from:"Шубарколь",to:"Аральск",cargo:"Оборудование",weight:"20 т",body:"бортовой",price:400000,pay:"jysan"},
  {date:"05.05",from:"Алматы",to:"Астана",cargo:"Продукты",weight:"3 т",body:"рефрижератор",price:290000,pay:"kaspi"},
  {date:"05.05",from:"Астана",to:"Павлодар",cargo:"Оборудование в ящиках",weight:"0.6 т",body:"тент",price:140000,pay:"kaspi"},
  {date:"05.05",from:"Астана",to:"Жезказган",cargo:"Плиты",weight:"20 т",body:"тент",price:240000,pay:"halyk"},
  {date:"06.05",from:"Кокшетау",to:"Павлодар",cargo:"Мешки на паллетах",weight:"16 т",body:"тент",price:210000,pay:"halyk"},
  {date:"06.05",from:"Кокшетау",to:"Бозшаколь",cargo:"Мешки на паллетах",weight:"14 т",body:"тент",price:195000,pay:"cash"},
  {date:"05.05",from:"Астана",to:"Петропавловск",cargo:"Металл",weight:"5.5 т",body:"металловоз",price:175000,pay:"halyk"},
  {date:"05.05",from:"Астана",to:"Кокшетау",cargo:"Сырье",weight:"5 т",body:"тент",price:120000,pay:"kaspi"},
  {date:"05.05",from:"Астана",to:"Астана",cargo:"Оборудование",weight:"20 т",body:"любой",price:60000,pay:"cash"},
  {date:"05.05",from:"Атырау",to:"Алматы",cargo:"Масло в бочках",weight:"0.6 т",body:"бензовоз",price:470000,pay:"halyk"},
  {date:"05.05",from:"Павлодар",to:"Балхаш",cargo:"Шины грузовые",weight:"7 т",body:"тент",price:280000,pay:"kaspi"},
  {date:"05.05",from:"Оскемен",to:"Алматы",cargo:"Оборудование",weight:"15 т",body:"крытая",price:430000,pay:"freedom"},
  {date:"05.05",from:"Шымкент",to:"Астана",cargo:"Посылка",weight:"10 т",body:"крытая",price:420000,pay:"kaspi"},
];
const transports=[
  {name:"Серик Ахметов",phone:"+7 701 234 56 78",city:"Астана",model:"Volvo FH16",body:"тент",cap:20,freeDate:"05.05",routes:"Астана – Алматы – Шымкент"},
  {name:"Канат Байжанов",phone:"+7 702 345 67 89",city:"Алматы",model:"MAN TGX 18.500",body:"крытая",cap:18,freeDate:"06.05",routes:"Алматы – Бишкек – Астана"},
  {name:"Алмас Нурланов",phone:"+7 777 456 78 90",city:"Павлодар",model:"КАМАЗ 5490",body:"тент",cap:15,freeDate:"05.05",routes:"Павлодар – Экибастуз – Астана"},
  {name:"Бауыржан Исаев",phone:"+7 707 567 89 01",city:"Шымкент",model:"DAF XF 105",body:"рефрижератор",cap:20,freeDate:"07.05",routes:"Шымкент – Алматы – Тараз"},
  {name:"Дастан Мухамеджанов",phone:"+7 708 678 90 12",city:"Астана",model:"Scania R500",body:"самосвал",cap:25,freeDate:"05.05",routes:"Астана – Жезказган – Балхаш"},
  {name:"Нурлан Сейткали",phone:"+7 771 789 01 23",city:"Алматы",model:"КАМАЗ 6520",body:"бортовой",cap:20,freeDate:"06.05",routes:"Алматы – Шымкент – Тараз"},
  {name:"Ерлан Касымов",phone:"+7 705 890 12 34",city:"Костанай",model:"MAN TGS 26.460",body:"зерновоз",cap:30,freeDate:"08.05",routes:"Костанай – Астана – Акмола"},
];

let myAddedLoads=[],myAddedTransports=[],currentUser=null;
let walletBalance=0,walletFrozen=0,transactions=[];
let pendingDeposits=[],pendingWithdrawals=[];
let currentOfferLoad={};
let selectedTransportForOrder=null;
let chats=[
  {id:1,route:"Астана → Алматы",cargo:"Продукты",status:"active",participants:["Компания","Водитель"],messages:[
    {from:"system",text:"Чат открыт по маршруту Астана → Алматы. Участники: Компания и Водитель.",time:"09:10"},
    {from:"company",text:"Здравствуйте, когда можете забрать груз?",time:"09:10"},
    {from:"driver",text:"Добрый день! Готов завтра с 8 утра.",time:"09:15"},
  ]},
];
let activeChatId=1;
let brokerActiveChatId=null;
let activeDeals=[];

let supportMessages=[];
let supportUnread=0;
let supportPanelOpen=false;
let supportActiveTab='guide';

let userRatings={};
let selectedRating=0;
let pendingRatingTarget=null;

let adminDeletedCount=0;
let adminNotifications=[];
let userWarnings={};


function fmt(v){return new Intl.NumberFormat("ru-KZ").format(v)+" ₸";}
function showToast(msg,type=""){
  const el=document.getElementById("toast");
  el.textContent=msg;el.className="toast"+(type?" "+type:"")+" show";
  setTimeout(()=>el.classList.remove("show"),2200);
}
function requireAuth(actionText){
  if(currentUser)return true;
  showToast(`Для действия "${actionText}" нужно войти в аккаунт`,"warn");
  openAuth();return false;
}
function phoneFormat(raw){
  const d=raw.replace(/\D/g,"");
  if(!d)return raw;
  const n=d.startsWith("7")?d:d.startsWith("8")?"7"+d.slice(1):d;
  const m=n.match(/^7(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})$/);
  if(!m)return"+"+n;
  let r="+7";
  if(m[1])r+=` (${m[1]}`;
  if(m[1].length===3)r+=")";
  if(m[2])r+=` ${m[2]}`;
  if(m[3])r+=" "+m[3];
  if(m[4])r+=" "+m[4];
  return r;
}
document.querySelectorAll(".phone-input").forEach(inp=>{
  inp.addEventListener("input",function(){this.value=phoneFormat(this.value);});
});
function nowTime(){
  const now=new Date();
  return `${String(now.getHours()).padStart(2,"0")}:${String(now.getMinutes()).padStart(2,"0")}`;
}


function switchTab(name){
  document.querySelectorAll(".tab-content").forEach(t=>t.classList.remove("active"));
  document.querySelectorAll(".nav-btn").forEach(b=>b.classList.toggle("active",b.dataset.tab===name));
  const el=document.getElementById("tab-"+name);
  if(el)el.classList.add("active");
  if(name==="chat-tab"&&currentUser){renderChatMessages();renderChatList();}
}
document.querySelectorAll(".nav-btn").forEach(b=>{
  b.addEventListener("click",()=>switchTab(b.dataset.tab));
});


const citySet=new Set();
loads.forEach(l=>{citySet.add(l.from);citySet.add(l.to);});
transports.forEach(t=>{citySet.add(t.city);});
const cities=["Все города",...Array.from(citySet).sort((a,b)=>a.localeCompare(b,"ru"))];
function fillSelect(id,opts){
  const el=document.getElementById(id);if(!el)return;
  el.innerHTML=opts.map(o=>`<option value="${o}">${o}</option>`).join("");
}
function fillBodySelect(id){
  const el=document.getElementById(id);if(!el)return;
  const hasSep=el.querySelector("option[value=all]");
  const base=hasSep?`<option value="all">Любой</option>`:"";
  el.innerHTML=base+["тент","крытая","изотерм","цельнометаллический","рефрижератор","автовоз","эвакуатор","автокран","бензовоз","бетоносмеситель","битумовоз","бортовой","бортовая","зерновоз","зерновоз-самосвал","контейнеровоз","коневоз","лесовоз","манипулятор","металловоз","микроавтобус грузовой","рефрижератор-самосвал","самосвал","трубовоз","фургон","экскаватор","автобус","любой"].map(b=>`<option value="${b}">${b}</option>`).join("");
}


function initDate(){
  function update(){
    const now=new Date();
    const dateStr=now.toLocaleDateString("ru-RU",{weekday:"long",day:"2-digit",month:"long",year:"numeric"});
    document.getElementById("todayDate").textContent=dateStr.charAt(0).toUpperCase()+dateStr.slice(1);
    const hh=String(now.getHours()).padStart(2,"0");
    const mm=String(now.getMinutes()).padStart(2,"0");
    const ss=String(now.getSeconds()).padStart(2,"0");
    document.getElementById("liveClock").textContent=`${hh}:${mm}:${ss}`;
  }
  update();setInterval(update,1000);
}


function initRatingStars(){
  const container=document.getElementById("ratingStars");
  container.innerHTML=[1,2,3,4,5].map(i=>`<button class="star-btn" data-val="${i}" onclick="setRating(${i})">☆</button>`).join("");
}
function setRating(val){
  selectedRating=val;
  document.querySelectorAll(".star-btn").forEach((s,i)=>{
    s.textContent=i<val?"★":"☆";
    s.style.color=i<val?"#f59e0b":"#94a3b8";
  });
  const labels=["","Плохо","Удовлетворительно","Нормально","Хорошо","Отлично"];
  document.getElementById("ratingValLabel").textContent=labels[val]||"";
}
document.getElementById("ratingFile").addEventListener("change",function(){
  document.getElementById("ratingFileName").textContent=this.files?.[0]?.name||"Файл не выбран";
});
function showRatingModal(targetName,targetType){
  pendingRatingTarget={name:targetName,type:targetType};
  selectedRating=0;
  document.getElementById("ratingTargetName").textContent=targetName;
  document.getElementById("ratingValLabel").textContent="Нажмите на звезду для оценки";
  document.getElementById("ratingComment").value="";
  document.getElementById("ratingFileName").textContent="Файл не выбран";
  document.querySelectorAll(".star-btn").forEach(s=>{s.textContent="☆";s.style.color="#94a3b8";});
  document.getElementById("ratingModal").classList.add("open");
}
function submitRating(){
  if(!selectedRating){showToast("Поставьте оценку","error");return;}
  const name=pendingRatingTarget?.name||"Неизвестно";
  if(!userRatings[name])userRatings[name]={total:0,count:0,reviews:[]};
  const file=document.getElementById("ratingFile").files?.[0];
  userRatings[name].total+=selectedRating;
  userRatings[name].count++;
  userRatings[name].reviews.unshift({
    rating:selectedRating,
    comment:document.getElementById("ratingComment").value.trim(),
    from:currentUser?`${currentUser.name} ${currentUser.surname||""}`.trim():"Аноним",
    time:nowTime(),
    file:file?.name||null
  });
  document.getElementById("ratingModal").classList.remove("open");
  showToast("Отзыв отправлен!","success");
  checkLowRatingAlert(name);
  renderProfile();renderTransports(transports);
  if(currentUser?.role==="admin")renderAdminPanel();
}
function getAvgRating(name){
  const r=userRatings[name];
  if(!r||!r.count)return null;
  return(r.total/r.count).toFixed(1);
}
function renderStarsDisplay(avg){
  if(!avg)return"";
  const val=parseFloat(avg);
  const full=Math.floor(val);
  let s="";
  for(let i=0;i<5;i++)s+=i<full?"★":"☆";
  return`<span class="rating-display"><span class="stars">${s}</span><span class="val">${avg}</span></span>`;
}
function checkLowRatingAlert(name){
  const avg=parseFloat(getAvgRating(name)||5);
  if(avg<=2.5){
    adminNotifications.push({type:"lowRating",name,avg:avg.toFixed(1),time:nowTime()});
    if(currentUser?.role==="admin")renderAdminPanel();
  }
}


function filterLoads(){
  const from=document.getElementById("fromCity").value;
  const to=document.getElementById("toCity").value;
  const body=document.getElementById("bodyType").value;
  const wt=document.getElementById("weightFilter").value;
  const pay=document.getElementById("payFilter").value;
  const minPrice=parseFloat(document.getElementById("minPriceFilter").value||"0");
  const filtered=loads.filter(item=>{
    return (from==="Все города"||item.from===from)&&
      (to==="Все города"||item.to===to)&&
      (body==="all"||item.body===body)&&
      (wt==="all"||parseFloat(item.weight)<=parseFloat(wt))&&
      (pay==="all"||item.pay===pay)&&
      (item.price>=minPrice);
  });
  renderTable(filtered);
  renderExpensive(filtered.length?filtered:loads);
  document.getElementById("resultsInfo").textContent=`Найдено грузов: ${filtered.length}`;
}
function renderTable(data){
  const tb=document.getElementById("loadsTable");
  if(!data.length){
    tb.innerHTML=`<tr><td colspan="8" class="muted" style="text-align:center;padding:1.5rem">По вашему запросу грузы не найдены.</td></tr>`;
    return;
  }
  tb.innerHTML=data.map(item=>`<tr>
    <td>${item.date}</td>
    <td><strong>${item.from}</strong> → <strong>${item.to}</strong></td>
    <td>${item.cargo}${item.company?`<div class="muted" style="font-size:.76rem">${item.company}</div>`:""}</td>
    <td>${item.weight}</td>
    <td><span class="tc-badge badge-blue">${item.body}</span></td>
    <td><span class="tc-badge badge-gold">${PAY_LABELS[item.pay]||item.pay}</span></td>
    <td><strong style="color:var(--primary)">${fmt(item.price)}</strong></td>
    <td style="white-space:nowrap">
      <span class="row-action" onclick="openLoadOfferFromIndex(${loads.indexOf(item)})">Откликнуться</span>
      <span class="dist-action" onclick="showDist('${item.from}','${item.to}')">Расстояние</span>
    </td>
  </tr>`).join("");
}
function renderExpensive(data){
  const today=new Date().toLocaleDateString("ru-RU",{day:"2-digit",month:"2-digit",year:"numeric"});
  document.getElementById("topLoadsTitle").textContent="Топ выгодных грузов за "+today;
  const scored=[...data].sort((a,b)=>b.price-a.price).slice(0,4);
  document.getElementById("expensiveLoads").innerHTML=scored.map(item=>{
    const dist=getDistance(item.from,item.to);
    const perKm=dist?Math.round(item.price/dist):0;
    return`<article class="expensive-card">
      <h3>${item.from} → ${item.to}</h3>
      <p>${item.cargo}, ${item.weight}, ${item.body}</p>
      <p class="price">${fmt(item.price)}</p>
      ${perKm?`<p style="font-size:.79rem;color:#7c3aed;font-weight:600;margin-top:.1rem">~${fmt(perKm)}/км · ${dist} км</p>`:""}
      <button class="btn accent sm quick-contact" data-from="${item.from}" data-to="${item.to}" data-price="${item.price}" data-cargo="${item.cargo}" data-weight="${item.weight}" data-company="${item.company||''}">Откликнуться</button>
    </article>`;
  }).join("");
}


function filterTransports(){
  const city=document.getElementById("tc-fromCity").value;
  const body=document.getElementById("tc-body").value;
  const cap=document.getElementById("tc-cap").value;
  const filtered=transports.filter(tr=>{
    return (city==="Все города"||tr.city===city)&&
      (body==="all"||tr.body===body)&&
      (cap==="all"||tr.cap<=parseFloat(cap));
  });
  renderTransports(filtered);
  document.getElementById("tc-resultsInfo").textContent=`Найдено: ${filtered.length}`;
}
function renderTransports(data){
  const el=document.getElementById("transportList");
  if(!data.length){
    el.innerHTML=`<div class="empty-state"><p>По вашему запросу транспорт не найден</p></div>`;
    return;
  }
  el.innerHTML=data.map(tr=>{
    const avg=getAvgRating(tr.name);
    const warnCount=userWarnings[tr.name]?.count||0;
    return`<div class="transport-card">
      <div class="tc-info">
        <div class="tc-header">
          <span class="tc-type">${tr.body}</span>
          <span class="tc-badge badge-green">Свободен с ${tr.freeDate}</span>
        </div>
        <p class="tc-driver">${tr.name}</p>
        ${avg?`<div style="margin-bottom:.3rem">${renderStarsDisplay(avg)}</div>`:""}
        ${warnCount>0?`<div class="tc-badge badge-red" style="margin-bottom:.3rem">⚠️ Предупреждений: ${warnCount}/3</div>`:""}
        <p class="tc-meta">${tr.model}<br>Грузоподъёмность: <strong>${tr.cap} т</strong><br>Город: ${tr.city}<br>Маршруты: ${tr.routes}</p>
        <div class="tc-actions">
          <button class="btn primary sm" onclick="openChatModal('${tr.name.replace(/'/g,"\\'")}','transport',null)">Перейти в чат</button>
          <button class="btn accent sm" onclick="openTransportOrder('${tr.name.replace(/'/g,"\\'")}')">Заказать</button>
          <button class="btn ghost sm" onclick="showRatingModal('${tr.name.replace(/'/g,"\\'")}','driver')">⭐ Отзыв</button>
        </div>
      </div>
    </div>`;
  }).join("");
}


function showDist(from,to){
  const dist=getDistance(from,to);
  document.getElementById("distRouteLabel").textContent=`${from} → ${to}`;
  const res=document.getElementById("distResult");
  if(dist!==null&&dist>0){
    document.getElementById("distKm").textContent=dist.toLocaleString("ru-RU");
    document.getElementById("distTime").textContent=`~${Math.round(dist/70)}–${Math.round(dist/60)} ч`;
    res.style.display="block";
  } else if(dist===0){
    document.getElementById("distKm").textContent="0 (в пределах города)";
    document.getElementById("distTime").textContent="< 1 ч";
    res.style.display="block";
  } else {
    res.style.display="none";
  }
  document.getElementById("distModal").classList.add("open");
}
document.getElementById("distModalClose").onclick=()=>document.getElementById("distModal").classList.remove("open");


document.getElementById("expensiveLoads").addEventListener("click",e=>{
  if(e.target.classList.contains("quick-contact")){
    openLoadOfferModal({
      from:e.target.dataset.from,to:e.target.dataset.to,
      price:parseFloat(e.target.dataset.price||"0"),
      cargo:e.target.dataset.cargo||"",weight:e.target.dataset.weight||"",
      company:e.target.dataset.company||"",
      idx:loads.findIndex(l=>l.from===e.target.dataset.from&&l.to===e.target.dataset.to&&String(l.price)===String(e.target.dataset.price))
    });
  }
});
document.getElementById("respondModalClose").onclick=()=>document.getElementById("respondModal").classList.remove("open");
document.getElementById("respondSubmitBtn").addEventListener("click",()=>{
  if(!requireAuth("отправка отклика"))return;
  const phone=document.getElementById("respondPhone").value.trim();
  const car=document.getElementById("respondCar").value.trim();
  if(!phone||!car){showToast("Укажите телефон и автомобиль","error");return;}
  document.getElementById("respondModal").classList.remove("open");
  document.getElementById("respondPhone").value="";
  document.getElementById("respondCar").value="";
  document.getElementById("respondComment").value="";
  showToast("Заявка отправлена. Брокер свяжет вас с заказчиком.","success");
});


function renderChatMessage(m,isBrokerView=false){
  if(m.from==="system"){
    return`<div class="chat-msg system">${m.text}<div class="chat-msg-meta">${m.time}</div></div>`;
  }
  if(m.from==="broker-msg"){
    if(!isBrokerView)return`<div class="chat-msg broker-msg"><strong>Брокер:</strong> ${m.text}<div class="chat-msg-meta">${m.time}</div></div>`;
    return`<div class="chat-msg broker-msg"><strong>Брокер · Гульназ Нуртай:</strong> ${m.text}<div class="chat-msg-meta">${m.time}</div></div>`;
  }
  const isMe=(m.from==="company"||m.from==="me");
  const label=m.from==="company"?"Компания":m.from==="driver"?"Водитель":m.from==="me"?"Вы":"Собеседник";
  return`<div class="chat-msg ${isMe?"mine":"other"}">
    <div>${m.text}</div>
    <div class="chat-msg-meta">${label} · ${m.time}</div>
  </div>`;
}
function renderChatMessages(){
  const chat=chats.find(c=>c.id===activeChatId)||chats[0];
  if(!chat)return;
  document.getElementById("chatRouteLabel").textContent=chat.route;
  const el=document.getElementById("chatMessages");
  el.innerHTML=chat.messages.map(m=>renderChatMessage(m,false)).join("");
  el.scrollTop=el.scrollHeight;
  renderChatList();
}
function renderChatList(){
  document.getElementById("chatList").innerHTML=chats.map(c=>{
    const last=c.messages.slice(-1)[0]||{text:"",time:""};
    const isActive=c.id===activeChatId;
    return`<div class="my-load-item" style="cursor:pointer;${isActive?"border-color:var(--primary);background:rgba(31,111,235,.04)":""}" onclick="activeChatId=${c.id};renderChatMessages()">
      <div class="my-load-info">
        <strong>${c.route}</strong>
        <span>${last.text.slice(0,35)}${last.text.length>35?"...":""}</span>
        <span style="color:var(--muted);font-size:.78rem">${last.time}</span>
      </div>
      <span class="tc-badge ${c.status==="active"?"badge-green":"badge-blue"}">${c.status==="active"?"Активен":"Завершён"}</span>
    </div>`;
  }).join("");
}
function sendChatMsg(){
  if(!requireAuth("отправка сообщения"))return;
  const inp=document.getElementById("chatInput");
  const text=inp.value.trim();if(!text)return;
  const chat=chats.find(c=>c.id===activeChatId)||chats[0];
  const from=currentUser?.role==="broker"?"broker-msg":"company";
  chat.messages.push({from,text,time:nowTime()});
  inp.value="";
  renderChatMessages();
  renderBrokerChatList();
  if(brokerActiveChatId===activeChatId)renderBrokerChatMessages();
}
function attachMainChatFile(input){
  if(!requireAuth("отправка файла"))return;
  const f=input.files?.[0];if(!f)return;
  const chat=chats.find(c=>c.id===activeChatId)||chats[0];
  chat.messages.push({from:"company",text:`📎 Файл: ${f.name}`,time:nowTime()});
  renderChatMessages();input.value="";
}
function confirmDelivery(){
  if(!currentUser){openAuth();return;}
  const chat=chats.find(c=>c.id===activeChatId)||chats[0];
  chat.messages.push({from:"driver",text:"Груз доставлен. Подтверждаю доставку.",time:nowTime()});
  chat.messages.push({from:"system",text:"Водитель подтвердил доставку груза. Ожидается подтверждение компании.",time:nowTime()});
  renderChatMessages();renderBrokerChatMessages();
  showToast("Доставка подтверждена. Ожидаем подтверждение компании.","warn");
}
function confirmReceipt(){
  if(!currentUser){openAuth();return;}
  const chat=chats.find(c=>c.id===activeChatId)||chats[0];
  chat.messages.push({from:"company",text:"Груз получен. Подтверждаю получение заказа.",time:nowTime()});
  chat.messages.push({from:"system",text:"Компания подтвердила получение. Сделка завершена. Средства разморожены.",time:nowTime()});
  chat.status="done";
  renderChatMessages();renderBrokerChatMessages();
  if(walletFrozen>0){
    const amount=walletFrozen;
    walletFrozen=0;
    transactions.unshift({type:"release",text:`Выплата по завершённой сделке`,amount:-amount,date:nowTime()});
    renderWallet();
  }
  showToast("Сделка завершена! Оцените водителя.","success");
  setTimeout(()=>showRatingModal(chat.participants?.[1]||"Водитель","driver"),800);
}


let activeChatModal={route:"",type:"",idx:null,chatId:null};
function openChatModal(route,type,idx){
  if(!requireAuth("чат и отклик"))return;
  let existingChat=chats.find(c=>c.route===route);
  if(!existingChat){
    const newId=Date.now();
    existingChat={id:newId,route,cargo:idx!==null&&loads[idx]?loads[idx].cargo:"",status:"active",participants:["Компания","Водитель"],messages:[
      {from:"system",text:`Чат открыт по маршруту ${route}. Контактные данные скрыты до подтверждения сделки.`,time:nowTime()},
    ]};
    chats.push(existingChat);
  }
  activeChatId=existingChat.id;
  activeChatModal={route,type,idx,chatId:existingChat.id};
  document.getElementById("chatModalTitle").textContent=type==="transport"?`Чат с водителем: ${route}`:`Чат по грузу: ${route}`;
  document.getElementById("chatModalSub").textContent="Контакты скрыты. Посредник наблюдает за диалогом.";
  document.getElementById("chatModalRoute").textContent=route;
  renderModalChatMessages();
  document.getElementById("chatModal").classList.add("open");
  renderBrokerChatList();
  renderChatList();
  if(idx!==null){
    brokerContactRequests.push({
      id:Date.now(),
      requester:currentUser?`${currentUser.name} ${currentUser.surname||""}`.trim():"Гость",
      requesterPhone:currentUser?.phone||"нет",
      route,type,time:nowTime(),status:"pending",
      cargoInfo:idx!==null&&loads[idx]?`${loads[idx].cargo}, ${loads[idx].weight}, ${loads[idx].body}`:"н/д",
      company:idx!==null&&loads[idx]?.company?loads[idx].company:"н/д",
      ownerPhone:idx!==null&&loads[idx]?.phone?loads[idx].phone:"н/д"
    });
    renderBrokerPanel();
  }
}
function renderModalChatMessages(){
  const el=document.getElementById("chatModalMessages");
  const chat=chats.find(c=>c.id===activeChatModal.chatId);
  const msgs=chat?.messages||[];
  el.innerHTML=msgs.map(m=>renderChatMessage(m,false)).join("");
  el.scrollTop=el.scrollHeight;
}
function sendModalChatMsg(){
  if(!requireAuth("отправка сообщения"))return;
  const inp=document.getElementById("chatModalInput");
  const text=inp.value.trim();if(!text)return;
  const chat=chats.find(c=>c.id===activeChatModal.chatId);
  if(chat){
    chat.messages.push({from:"me",text,time:nowTime()});
  }
  inp.value="";
  renderModalChatMessages();
  renderBrokerChatList();
  if(brokerActiveChatId===activeChatModal.chatId)renderBrokerChatMessages();
  if(activeChatId===activeChatModal.chatId)renderChatMessages();
  setTimeout(()=>{
    if(chat){
      chat.messages.push({from:"other",text:"Получил ваше сообщение. Уточняю детали.",time:nowTime()});
      renderModalChatMessages();
      if(activeChatId===activeChatModal.chatId)renderChatMessages();
      if(brokerActiveChatId===activeChatModal.chatId)renderBrokerChatMessages();
    }
  },1500);
}
function useSuggestion(el){
  document.getElementById("chatModalInput").value=el.textContent;
  document.getElementById("chatModalInput").focus();
}
function attachModalChatFile(input){
  if(!requireAuth("отправка файла"))return;
  const f=input.files?.[0];if(!f)return;
  const chat=chats.find(c=>c.id===activeChatModal.chatId);
  if(chat)chat.messages.push({from:"me",text:`📎 Файл: ${f.name}`,time:nowTime()});
  renderModalChatMessages();input.value="";
  if(activeChatId===activeChatModal.chatId)renderChatMessages();
}
function requestBrokerContact(){
  if(!currentUser){openAuth();return;}
  const chat=chats.find(c=>c.id===activeChatModal.chatId);
  if(chat)chat.messages.push({from:"system",text:"Пользователь запросил контакты у посредника. Брокер рассматривает запрос.",time:nowTime()});
  renderModalChatMessages();renderBrokerChatMessages();
  showToast("Запрос отправлен посреднику Гульназ Нуртай","success");
}
function confirmDealInChat(){
  if(!currentUser){openAuth();return;}
  const load=activeChatModal.idx!==null?loads[activeChatModal.idx]:null;
  const commission=load?Math.round(load.price*0.01):5000;
  if(walletBalance<commission){showToast(`Недостаточно средств. Нужно ${fmt(commission)} (1%)`,"error");return;}
  walletBalance-=commission;
  brokerWalletBalance+=commission;
  brokerTransactions.unshift({text:`Комиссия от сделки: ${activeChatModal.route}`,amount:commission,date:nowTime()});
  brokerDealsCompleted++;
  transactions.unshift({type:"withdraw",text:`Комиссия посредника (1%) — ${activeChatModal.route}`,amount:-commission,date:nowTime()});
  activeDeals.push({id:Date.now(),route:activeChatModal.route,cargo:load?load.cargo:"",price:load?load.price:0,commission,time:nowTime(),status:"active",chatId:activeChatModal.chatId});
  const chat=chats.find(c=>c.id===activeChatModal.chatId);
  if(chat)chat.messages.push({from:"system",text:`Компания подтвердила сделку и оплатила комиссию (1%). Ожидается подтверждение водителя.`,time:nowTime()});
  renderModalChatMessages();renderWallet();renderBrokerPanel();renderBrokerChatMessages();
  showToast(`Сделка подтверждена! Комиссия ${fmt(commission)} переведена посреднику.`,"success");
}


function respondFromMapModal(){
  document.getElementById("loadOfferModal").classList.remove("open");
  setTimeout(()=>{
    openChatModal(currentOfferLoad.from+" → "+currentOfferLoad.to,"load",currentOfferLoad.idx);
  },180);
}
function openLoadOfferModal(load){
  if(!requireAuth("отклик на груз"))return;
  currentOfferLoad=load;
  const dist=getDistance(load.from,load.to)||0;
  const route=`${load.from} → ${load.to}`;
  const mapUrl=`https://maps.google.com/maps?q=${encodeURIComponent(load.from+", Казахстан")}+to+${encodeURIComponent(load.to+", Казахстан")}&output=embed`;
  document.getElementById("loadOfferSub").textContent=`${route} · ${dist?dist+" км":"расстояние не найдено"}`;
  document.getElementById("loadOfferMap").src=mapUrl;
  document.getElementById("loadOfferDetails").innerHTML=`<h4>Детали груза</h4>
    <div style="font-size:.86rem;line-height:1.7">
      Компания: <strong>${load.company||"н/д"}</strong><br>
      Груз: <strong>${load.cargo||"н/д"}</strong><br>
      Вес: <strong>${load.weight||"н/д"}</strong><br>
      Оплата: <strong>${fmt(load.price||0)}</strong><br>
      Эффективность: <strong>${dist?Math.round((load.price||0)/dist)+" тнг/км":"н/д"}</strong>
    </div>`;
  document.getElementById("loadOfferCosts").value="";
  document.getElementById("loadOfferProfit").value=fmt(load.price||0);
  document.getElementById("loadOfferModal").classList.add("open");
}
function openLoadOfferFromIndex(idx){
  const l=loads[idx];if(!l)return;
  openLoadOfferModal({from:l.from,to:l.to,price:l.price,cargo:l.cargo,weight:l.weight,company:l.company||"Компания не указана",idx});
}
function recalcLoadProfit(){
  const revenue=currentOfferLoad.price||0;
  const costs=parseFloat(document.getElementById("loadOfferCosts").value||"0");
  document.getElementById("loadOfferProfit").value=fmt(Math.max(revenue-costs,0));
}


function openTransportOrder(driverName){
  if(!requireAuth("заказ транспорта"))return;
  selectedTransportForOrder=transports.find(t=>t.name===driverName)||null;
  const el=document.getElementById("transportExistingOffers");
  if(!myAddedLoads.length){
    el.innerHTML=`<p class="muted" style="text-align:center;padding:.8rem">У вас нет добавленных грузов. <a style="color:var(--primary);cursor:pointer" onclick="document.getElementById('transportOrderModal').classList.remove('open');switchTab('add-load')">Добавить груз →</a></p>`;
  } else {
    el.innerHTML=myAddedLoads.map((l,idx)=>`
      <div class="my-load-item">
        <div class="my-load-info"><strong>${l.from} → ${l.to}</strong><span>${l.cargo} · ${l.weight} · ${fmt(l.price)}</span></div>
        <button class="btn ghost sm" onclick="pickExistingOffer(${idx})">Выбрать</button>
      </div>`).join("");
  }
  document.getElementById("transportOrderModal").classList.add("open");
}
function pickExistingOffer(idx){
  const l=myAddedLoads[idx];if(!l)return;
  document.getElementById("to-from").value=l.from;
  document.getElementById("to-to").value=l.to;
  document.getElementById("to-price").value=l.price;
  document.getElementById("to-company").value=l.company||"";
  document.getElementById("to-notes").value=`${l.cargo}, ${l.weight}, ${l.body}`;
}
function submitTransportOrder(){
  if(!selectedTransportForOrder){showToast("Сначала выберите водителя","error");return;}
  const from=document.getElementById("to-from").value.trim();
  const to=document.getElementById("to-to").value.trim();
  const price=document.getElementById("to-price").value.trim();
  const phone=document.getElementById("to-phone").value.trim();
  if(!from||!to||!price||!phone){showToast("Заполните обязательные поля","error");return;}
  document.getElementById("transportOrderModal").classList.remove("open");
  setTimeout(()=>{openChatModal(`${selectedTransportForOrder.name}: ${from} → ${to}`,"transport",null);},180);
  showToast("Заказ отправлен водителю в чат","success");
}


function renderBrokerChatList(){
  const el=document.getElementById("brokerChatList");if(!el)return;
  if(!chats.length){el.innerHTML=`<p class="muted" style="text-align:center;padding:1rem;font-size:.84rem">Чатов пока нет</p>`;return;}
  el.innerHTML=chats.map(c=>{
    const last=c.messages.slice(-1)[0]||{text:"",time:""};
    const isActive=brokerActiveChatId===c.id;
    return`<div class="broker-chat-item ${isActive?"active":""}" onclick="selectBrokerChat(${c.id})">
      <strong>${c.route}</strong>
      <span>${last.text.slice(0,40)}${last.text.length>40?"...":""}</span>
      <span style="font-size:.74rem;color:var(--muted);margin-top:.15rem;display:block">${last.time}</span>
    </div>`;
  }).join("");
}
function selectBrokerChat(id){
  brokerActiveChatId=id;
  const chat=chats.find(c=>c.id===id);
  if(chat){
    document.getElementById("brokerActiveChatLabel").textContent=chat.route;
    document.getElementById("brokerActiveChatStatus").textContent=chat.status==="active"?"Активен":"Завершён";
    document.getElementById("brokerActiveChatStatus").className=`tc-badge ${chat.status==="active"?"badge-green":"badge-blue"}`;
  }
  renderBrokerChatMessages();renderBrokerChatList();
}
function renderBrokerChatMessages(){
  const el=document.getElementById("brokerChatMessages");if(!el)return;
  if(!brokerActiveChatId){
    el.innerHTML=`<div style="text-align:center;color:var(--muted);padding:2rem;font-size:.86rem">Выберите чат из списка слева</div>`;
    return;
  }
  const chat=chats.find(c=>c.id===brokerActiveChatId);
  if(!chat){el.innerHTML="";return;}
  el.innerHTML=chat.messages.map(m=>{
    if(m.from==="system")return`<div class="chat-msg system">${m.text}<div class="chat-msg-meta">${m.time}</div></div>`;
    if(m.from==="broker-msg")return`<div class="chat-msg broker-msg"><strong>Брокер:</strong> ${m.text}<div class="chat-msg-meta">${m.time}</div></div>`;
    const label=m.from==="company"?"Компания":m.from==="driver"?"Водитель":m.from==="me"?"Пользователь":"Собеседник";
    return`<div class="chat-msg other" style="max-width:80%">
      <div style="font-size:.74rem;font-weight:700;color:var(--primary);margin-bottom:.2rem">${label}</div>
      <div>${m.text}</div>
      <div class="chat-msg-meta">${m.time}</div>
    </div>`;
  }).join("");
  el.scrollTop=el.scrollHeight;
}
function sendBrokerChatMsg(){
  if(!brokerActiveChatId){showToast("Выберите чат","warn");return;}
  const inp=document.getElementById("brokerChatInput");
  const text=inp.value.trim();if(!text)return;
  const chat=chats.find(c=>c.id===brokerActiveChatId);if(!chat)return;
  chat.messages.push({from:"broker-msg",text,time:nowTime()});
  inp.value="";
  renderBrokerChatMessages();renderBrokerChatList();
  if(activeChatModal.chatId===brokerActiveChatId)renderModalChatMessages();
  if(activeChatId===brokerActiveChatId)renderChatMessages();
}


let walletModalMode="deposit";
const BANK_REQUISITES={
  kaspi:{phone:"+7 777 777 7777",card:"7777 7777 7777 7777"},
  halyk:{phone:"+7 777 777 7777",card:"7777 7777 7777 7777"},
  freedom:{phone:"+7 777 777 7777",card:"7777 7777 7777 7777"},
  jysan:{phone:"+7 777 777 7777",card:"7777 7777 7777 7777"},
  bes:{phone:"+7 777 777 7777",card:"7777 7777 7777 7777"},
  forte:{phone:"+7 777 777 7777",card:"7777 7777 7777 7777"},
  eurasian:{phone:"+7 777 777 7777",card:"7777 7777 7777 7777"},
  atf:{phone:"+7 777 777 7777",card:"7777 7777 7777 7777"},
  centerc:{phone:"+7 777 777 7777",card:"7777 7777 7777 7777"},
  nurdaulet:{phone:"+7 777 777 7777",card:"7777 7777 7777 7777"},
};
function openWalletModal(mode){
  if(!requireAuth(mode==="deposit"?"пополнение кошелька":"вывод средств"))return;
  walletModalMode=mode;
  document.getElementById("walletModalTitle").textContent=mode==="deposit"?"Пополнение кошелька":"Вывод средств";
  document.getElementById("walletModalSub").textContent=mode==="deposit"?"Выберите банк, оплатите по реквизитам и приложите чек":"Заполните данные получателя для вывода";
  document.getElementById("walletFeeText").textContent=mode==="deposit"?"Комиссия за пополнение: 5%":"Комиссия за вывод: 0%";
  document.getElementById("walletReceiptWrap").style.display=mode==="deposit"?"grid":"none";
  document.getElementById("walletRequisites").style.display=mode==="deposit"?"block":"none";
  document.getElementById("walletWithdrawDetails").style.display=mode==="withdraw"?"block":"none";
  document.getElementById("walletReceipt").value="";
  document.getElementById("walletReceiptName").textContent="Файл не выбран";
  document.getElementById("walletAmount").value="";
  updateWalletRequisites();
  document.getElementById("walletModal").classList.add("open");
}
function updateWalletRequisites(){
  const bank=document.getElementById("walletBank").value;
  const req=BANK_REQUISITES[bank]||BANK_REQUISITES.kaspi;
  document.getElementById("walletReqPhone").textContent=req.phone;
  document.getElementById("walletReqCard").textContent=req.card;
}
document.getElementById("walletBank").addEventListener("change",updateWalletRequisites);
document.getElementById("walletReceipt").addEventListener("change",()=>{
  const file=document.getElementById("walletReceipt").files?.[0];
  document.getElementById("walletReceiptName").textContent=file?`Выбран: ${file.name}`:"Файл не выбран";
});
document.getElementById("walletConfirmBtn").addEventListener("click",()=>{
  const amount=parseFloat(document.getElementById("walletAmount").value);
  if(!amount||amount<1000){showToast("Минимальная сумма 1000 тнг","error");return;}
  const bank=document.getElementById("walletBank").value;
  if(walletModalMode==="deposit"){
    const receipt=document.getElementById("walletReceipt").files?.[0];
    if(!receipt){showToast("Прикрепите чек для пополнения","error");return;}
    const fee=Math.round(amount*0.05);
    pendingDeposits.unshift({id:Date.now(),user:currentUser.name,phone:currentUser.phone,bank,amount,fee,net:amount-fee,receipt:receipt.name,date:nowTime(),status:"pending"});
    showToast("Пополнение отправлено посреднику на одобрение","warn");
  } else {
    const firstName=document.getElementById("withdrawFirstName").value.trim();
    const lastName=document.getElementById("withdrawLastName").value.trim();
    const outPhone=document.getElementById("withdrawPhone").value.trim();
    const outCard=document.getElementById("withdrawCard").value.trim();
    if(!firstName||!lastName||!outPhone||!outCard){showToast("Заполните все поля для вывода","error");return;}
    pendingWithdrawals.unshift({id:Date.now(),user:currentUser.name,phone:currentUser.phone,bank,amount,date:nowTime(),status:"pending",firstName,lastName,outPhone,outCard});
    showToast("Вывод отправлен посреднику на одобрение","warn");
  }
  document.getElementById("walletModal").classList.remove("open");
  renderBrokerPanel();renderWallet();
});
async function copyWalletValue(id){
  const value=document.getElementById(id)?.textContent?.trim();if(!value)return;
  try{await navigator.clipboard.writeText(value);}catch(e){
    const tmp=document.createElement("textarea");tmp.value=value;document.body.appendChild(tmp);tmp.select();document.execCommand("copy");document.body.removeChild(tmp);
  }
  showToast("Скопировано в буфер обмена","success");
}
function renderWallet(){
  document.getElementById("walletBalance").textContent=fmt(walletBalance);
  document.getElementById("walletFrozen").textContent=walletFrozen>0?`На удержании (эскроу): ${fmt(walletFrozen)}`:"";
  const txEl=document.getElementById("txList");
  txEl.innerHTML=transactions.length?transactions.slice(0,15).map(tx=>`
    <div class="tx-item">
      <span>${tx.text}</span>
      <span class="${tx.type==="deposit"?"tx-plus":tx.type==="frozen"?"tx-frozen":"tx-minus"}">${tx.amount>0?"+":""}${fmt(Math.abs(tx.amount))}</span>
      <span class="muted" style="font-size:.78rem">${tx.date}</span>
    </div>`).join(""):`<p class="muted" style="text-align:center;padding:1rem">История транзакций пуста</p>`;
}


document.getElementById("al-submitBtn").addEventListener("click",()=>{
  if(!requireAuth("размещение груза"))return;
  const from=document.getElementById("al-from").value;
  const to=document.getElementById("al-to").value;
  const cargo=document.getElementById("al-cargo").value.trim();
  const weight=document.getElementById("al-weight").value;
  const price=document.getElementById("al-price").value;
  const phone=document.getElementById("al-phone").value.trim();
  if(!cargo||!weight||!price||!phone){showToast("Заполните все обязательные поля","error");return;}
  const date=document.getElementById("al-date").value;
  const d=date?new Date(date).toLocaleDateString("ru-RU",{day:"2-digit",month:"2-digit"}):"05.05";
  const newLoad={date:d,from,to,cargo,weight:`${weight} т`,body:document.getElementById("al-body").value,
    price:parseFloat(price),pay:document.getElementById("al-pay").value,phone,
    company:document.getElementById("al-company").value.trim(),mine:true};
  loads.unshift(newLoad);myAddedLoads.unshift(newLoad);
  document.getElementById("al-success").classList.add("show");
  setTimeout(()=>document.getElementById("al-success").classList.remove("show"),4000);
  showToast("Груз размещён в ленте!","success");
  filterLoads();if(currentUser)renderProfile();
  if(walletBalance>=parseFloat(price)){
    walletBalance-=parseFloat(price);walletFrozen+=parseFloat(price);
    transactions.unshift({type:"frozen",text:`Заморожено для заказа ${from} → ${to}`,amount:-parseFloat(price),date:nowTime()});
    renderWallet();
  }
});
document.getElementById("al-resetBtn").addEventListener("click",()=>{
  document.querySelectorAll("#tab-add-load input[type=text],#tab-add-load input[type=number],#tab-add-load input[type=date],#tab-add-load textarea").forEach(el=>el.value="");
});


document.getElementById("at-submitBtn").addEventListener("click",()=>{
  if(!requireAuth("добавление транспорта"))return;
  const name=document.getElementById("at-name").value.trim();
  const phone=document.getElementById("at-phone").value.trim();
  const model=document.getElementById("at-model").value.trim();
  const cap=document.getElementById("at-cap").value;
  const city=document.getElementById("at-city").value.trim();
  if(!name||!phone||!model||!cap||!city){showToast("Заполните все обязательные поля","error");return;}
  const newT={name,phone,model,body:document.getElementById("at-body").value,
    cap:parseFloat(cap),city,routes:document.getElementById("at-routes").value,freeDate:"сегодня",mine:true};
  transports.unshift(newT);myAddedTransports.unshift(newT);
  document.getElementById("at-success").classList.add("show");
  setTimeout(()=>document.getElementById("at-success").classList.remove("show"),4000);
  showToast("Транспорт добавлен в поиск!","success");
  renderTransports(transports);if(currentUser)renderProfile();
});
document.getElementById("at-resetBtn").addEventListener("click",()=>{
  document.querySelectorAll("#tab-add-transport input[type=text],#tab-add-transport input[type=number],#tab-add-transport input[type=date]").forEach(el=>el.value="");
});


document.getElementById("findBtn").addEventListener("click",filterLoads);
document.getElementById("tc-findBtn").addEventListener("click",filterTransports);
document.getElementById("resetFiltersBtn").addEventListener("click",()=>{
  document.getElementById("fromCity").value="Все города";
  document.getElementById("toCity").value="Все города";
  document.getElementById("bodyType").value="all";
  document.getElementById("weightFilter").value="all";
  document.getElementById("payFilter").value="all";
  document.getElementById("minPriceFilter").value="";
  filterLoads();showToast("Фильтры сброшены");
});
document.getElementById("showAllExpensiveBtn").addEventListener("click",()=>{
  renderExpensive(loads);showToast("Показаны все дорогие грузы");
});


let userProfiles={};
function openProfileEdit(){
  if(!currentUser)return;
  const prof=userProfiles[currentUser.phone]||{};
  document.getElementById("editName").value=currentUser.name||"";
  document.getElementById("editSurname").value=currentUser.surname||"";
  document.getElementById("editPhone").value=currentUser.phone||"";
  document.getElementById("editEmail").value=prof.email||"";
  document.getElementById("editCompany").value=prof.company||"";
  document.getElementById("editCompanyLabel").style.display="grid";
  document.getElementById("editCompanyLabel").querySelector("input").placeholder=currentUser.role==="shipper"?"ТОО Астана Логистик (обязательно)":"Компания (необязательно)";
  const verifyStatus=prof.verifyStatus||"none";
  const statusLabels={none:"Не верифицирован",pending:"На проверке",approved:"Верифицирован ✓"};
  const statusClasses={none:"pv-none",pending:"pv-pending",approved:"pv-approved"};
  document.getElementById("currentVerifyStatus").innerHTML=`Текущий статус: <span class="profile-verify-badge ${statusClasses[verifyStatus]}">${statusLabels[verifyStatus]}</span>`;
  document.getElementById("verifyDocFile").value="";
  document.getElementById("verifyDocFileName").textContent="Файл не выбран";
  document.getElementById("profileEditModal").classList.add("open");
}
document.getElementById("verifyDocFile").addEventListener("change",function(){
  document.getElementById("verifyDocFileName").textContent=this.files?.[0]?.name||"Файл не выбран";
});
function saveProfileEdit(){
  if(!currentUser)return;
  const name=document.getElementById("editName").value.trim();
  const surname=document.getElementById("editSurname").value.trim();
  const email=document.getElementById("editEmail").value.trim();
  const company=document.getElementById("editCompany").value.trim();
  if(currentUser.role==="shipper"&&!company){showToast("Название компании обязательно для грузоотправителей","error");return;}
  if(!name){showToast("Укажите имя","error");return;}
  currentUser.name=name;currentUser.surname=surname;
  if(!userProfiles[currentUser.phone])userProfiles[currentUser.phone]={};
  userProfiles[currentUser.phone].email=email;
  userProfiles[currentUser.phone].company=company;
  const docFile=document.getElementById("verifyDocFile").files?.[0];
  if(docFile){
    const docType=document.querySelector('input[name="verifyDocType"]:checked')?.value||"passport";
    userProfiles[currentUser.phone].verifyStatus="pending";
    userProfiles[currentUser.phone].verifyDoc=docFile.name;
    userProfiles[currentUser.phone].verifyDocType=docType;
    showToast("Документ отправлен на проверку. Ожидайте верификации.","warn");
  }
  localStorage.setItem("nurtay_session",JSON.stringify(currentUser));
  const users=JSON.parse(localStorage.getItem("nurtay_users")||"[]");
  const idx=users.findIndex(u=>u.phone===currentUser.phone);
  if(idx>-1){users[idx]=currentUser;localStorage.setItem("nurtay_users",JSON.stringify(users));}
  document.getElementById("profileEditModal").classList.remove("open");
  showToast("Профиль обновлён!","success");
  renderProfile();
  document.getElementById("profileName").textContent=currentUser.name;
  document.getElementById("userGreeting").textContent=currentUser.name;
  const initials=(currentUser.name[0]+(currentUser.surname?.[0]||"")).toUpperCase();
  document.getElementById("avatarLetter").textContent=initials;
  document.getElementById("bigAvatar").textContent=initials;
}


function openAuth(tab="login"){
  document.getElementById("authModal").classList.add("open");
  switchAuthTab(tab);
}
function closeAuth(){document.getElementById("authModal").classList.remove("open");}
document.getElementById("authBtn").addEventListener("click",()=>openAuth());
document.getElementById("profileAuthBtn").addEventListener("click",()=>openAuth());
document.getElementById("authModalClose").addEventListener("click",closeAuth);
document.getElementById("authModal").addEventListener("click",e=>{if(e.target.id==="authModal")closeAuth();});
function switchAuthTab(tab){
  document.querySelectorAll(".auth-tab-btn").forEach(b=>b.classList.toggle("active",b.dataset.auth===tab));
  document.getElementById("authFormLogin").classList.toggle("active",tab==="login");
  document.getElementById("authFormRegister").classList.toggle("active",tab==="register");
}
document.querySelectorAll(".auth-tab-btn").forEach(b=>b.addEventListener("click",()=>switchAuthTab(b.dataset.auth)));
document.getElementById("toRegisterLink").addEventListener("click",()=>switchAuthTab("register"));
document.getElementById("toLoginLink").addEventListener("click",()=>switchAuthTab("login"));

const PROTECTED_PHONES=["+77058846446","77058846446","87058846446"];
const BROKER_WHITELIST=[{name:"Гульназ",surname:"Нуртай",contact:"+77058846446",pwd:"Gnurtay123!"}];
const MAIN_BROKER=BROKER_WHITELIST[0];
// ✅ UPDATED ADMIN PASSWORD
const ADMIN_PWD="Gnurtay123!";

document.getElementById("loginSubmitBtn").addEventListener("click",()=>{
  const phoneInput=document.getElementById("loginPhone").value.trim();
  const pwd=document.getElementById("loginPwd").value;
  const err=document.getElementById("loginError");err.classList.remove("show");
  const normalizePhone=s=>s.replace(/\D/g,"").slice(-10);
  const phoneNorm=normalizePhone(phoneInput);
  const isBroker=PROTECTED_PHONES.map(p=>normalizePhone(p)).includes(phoneNorm)&&pwd===MAIN_BROKER.pwd;
  if(isBroker){
    const brokerUser={name:"Гульназ",surname:"Нуртай",phone:"+77058846446",pwd,role:"broker"};
    setUser(brokerUser);closeAuth();
    switchTab("broker");showToast("Добро пожаловать, Гульназ Нуртай!","success");
    renderBrokerPanel();renderProfile();return;
  }
  const stored=JSON.parse(localStorage.getItem("nurtay_users")||"[]");
  const user=stored.find(u=>normalizePhone(u.phone||"")===phoneNorm&&u.pwd===pwd);
  if(!user){err.classList.add("show");return;}
  setUser(user);closeAuth();showToast(`Добро пожаловать, ${user.name}!`,"success");renderProfile();
});
document.getElementById("registerSubmitBtn").addEventListener("click",()=>{
  const name=document.getElementById("regName").value.trim();
  const surname=document.getElementById("regSurname").value.trim();
  const phone=document.getElementById("regPhone").value.trim();
  const pwd=document.getElementById("regPwd").value;
  const pwd2=document.getElementById("regPwd2").value;
  const role=document.getElementById("regRole").value;
  const err=document.getElementById("registerError");err.classList.remove("show");
  if(!name||!surname||!phone||!pwd){err.textContent="Заполните все поля";err.classList.add("show");return;}
  if(pwd.length<6){err.textContent="Пароль минимум 6 символов";err.classList.add("show");return;}
  if(pwd!==pwd2){err.textContent="Пароли не совпадают";err.classList.add("show");return;}
  const normalizePhone=s=>s.replace(/\D/g,"").slice(-10);
  if(PROTECTED_PHONES.map(p=>normalizePhone(p)).includes(normalizePhone(phone))){
    err.textContent="Этот номер уже зарегистрирован";err.classList.add("show");return;
  }
  const users=JSON.parse(localStorage.getItem("nurtay_users")||"[]");
  if(users.find(u=>normalizePhone(u.phone||"")===normalizePhone(phone))){
    err.textContent="Этот номер уже зарегистрирован";err.classList.add("show");return;
  }
  const newUser={name,surname,phone,pwd,role};
  users.push(newUser);localStorage.setItem("nurtay_users",JSON.stringify(users));
  setUser(newUser);closeAuth();showToast(`Аккаунт создан! Добро пожаловать, ${name}!`,"success");renderProfile();
});

function setUser(user){
  currentUser=user;
  const initials=(user.name[0]+(user.surname?.[0]||"")).toUpperCase();
  document.getElementById("authBtn").style.display="none";
  document.getElementById("profileBadge").classList.add("show");
  document.getElementById("avatarLetter").textContent=initials;
  document.getElementById("profileName").textContent=user.name;
  document.getElementById("userGreeting").textContent=user.name;
  document.getElementById("userGreeting").style.display="block";
  localStorage.setItem("nurtay_session",JSON.stringify(user));
  updateBrokerAccessUI();updateAdminAccessUI();
  document.getElementById("walletGuest").style.display="none";
  document.getElementById("walletUser").style.display="block";
  document.getElementById("chatGuest").style.display="none";
  document.getElementById("chatUser").style.display="block";
  refreshChatRoleUI();
  renderWallet();renderChatMessages();renderChatList();
}
document.getElementById("logoutBtn").addEventListener("click",()=>{
  currentUser=null;
  document.getElementById("authBtn").style.display="";
  document.getElementById("profileBadge").classList.remove("show");
  document.getElementById("userGreeting").style.display="none";
  localStorage.removeItem("nurtay_session");
  document.getElementById("walletGuest").style.display="block";
  document.getElementById("walletUser").style.display="none";
  document.getElementById("chatGuest").style.display="block";
  document.getElementById("chatUser").style.display="none";
  updateBrokerAccessUI();updateAdminAccessUI();
  renderProfile();showToast("Вы вышли из аккаунта");
});


function renderProfile(){
  const guest=document.getElementById("profileGuest");
  const user=document.getElementById("profileUser");
  if(!currentUser){guest.style.display="block";user.style.display="none";return;}
  guest.style.display="none";user.style.display="block";
  const prof=userProfiles[currentUser.phone]||{};
  document.getElementById("profileFullName").textContent=`${currentUser.name} ${currentUser.surname||""}`;
  document.getElementById("profileEmail").textContent=prof.email||currentUser.phone||"";
  const roleLabel={shipper:"Грузоотправитель / Компания",carrier:"Перевозчик / Водитель",broker:"Брокер / Посредник",admin:"Администратор"}[currentUser.role]||currentUser.role;
  document.getElementById("profileRoleBadge").innerHTML=`<span class="tc-badge badge-blue">${roleLabel}</span>`;
  const initials=(currentUser.name[0]+(currentUser.surname?.[0]||"")).toUpperCase();
  document.getElementById("bigAvatar").textContent=initials;
  const compEl=document.getElementById("profileCompanyDisplay");
  const prof2=userProfiles[currentUser.phone]||{};
  compEl.textContent=prof2.company?`🏢 ${prof2.company}`:"";
  const verifyEl=document.getElementById("profileVerifyBadge");
  const vs=prof.verifyStatus||"none";
  if(vs==="approved")verifyEl.innerHTML=`<span class="profile-verify-badge pv-approved">✓ Личность подтверждена</span>`;
  else if(vs==="pending")verifyEl.innerHTML=`<span class="profile-verify-badge pv-pending">⏳ Верификация на проверке</span>`;
  else verifyEl.innerHTML=`<span class="profile-verify-badge pv-none">Не верифицирован</span>`;
  const avg=getAvgRating(`${currentUser.name} ${currentUser.surname||""}`.trim());
  document.getElementById("profileRatingDisplay").innerHTML=avg?`Рейтинг: ${renderStarsDisplay(avg)}`:"";

  const ml=document.getElementById("myLoadsList");
  ml.innerHTML=myAddedLoads.length
    ?myAddedLoads.map((l,i)=>`
      <div class="my-load-item">
        <div class="my-load-info">
          <strong>${l.from} → ${l.to}</strong>
          <span>${l.cargo} · ${l.weight} · ${l.body}${l.company?` · ${l.company}`:""}</span>
        </div>
        <div class="my-load-actions">
          <span class="my-load-price">${fmt(l.price)}</span>
          <span class="tc-badge badge-green">Активна</span>
          <button class="btn ghost sm" onclick="openEditLoad(${i})" style="padding:.25rem .55rem;font-size:.76rem">✏️</button>
          <button class="btn sm" onclick="deleteMyLoad(${i})" style="padding:.25rem .55rem;font-size:.76rem;background:var(--danger);color:#fff;border-color:var(--danger)">🗑</button>
        </div>
      </div>`).join("")
    :`<div class="empty-state"><div class="es-icon">📦</div><p>Вы ещё не добавляли грузы</p></div>`;

  const mt=document.getElementById("myTransportList");
  mt.innerHTML=myAddedTransports.length
    ?myAddedTransports.map((tr,i)=>`
      <div class="my-load-item">
        <div class="my-load-info">
          <strong>${tr.model}</strong>
          <span>${tr.body} · ${tr.cap} т · ${tr.city}</span>
        </div>
        <div class="my-load-actions">
          <span class="tc-badge badge-green">Свободен</span>
          <button class="btn ghost sm" onclick="openEditTransport(${i})" style="padding:.25rem .55rem;font-size:.76rem">✏️</button>
          <button class="btn sm" onclick="deleteMyTransport(${i})" style="padding:.25rem .55rem;font-size:.76rem;background:var(--danger);color:#fff;border-color:var(--danger)">🗑</button>
        </div>
      </div>`).join("")
    :`<div class="empty-state"><div class="es-icon">🚛</div><p>Вы ещё не добавляли транспорт</p></div>`;

  const myFullName=`${currentUser.name} ${currentUser.surname||""}`.trim();
  const reviews=userRatings[myFullName]?.reviews||[];
  const reviewsCard=document.getElementById("myReviewsCard");
  if(reviews.length){
    reviewsCard.style.display="block";
    document.getElementById("myReviewsList").innerHTML=reviews.map(r=>`
      <div class="review-card">
        <div class="rev-head">
          <span>${r.from}</span>
          <span style="color:#f59e0b">${"★".repeat(r.rating)}${"☆".repeat(5-r.rating)}</span>
        </div>
        ${r.comment?`<p>${r.comment}</p>`:""}
        ${r.file?`<p style="font-size:.76rem;color:var(--muted)">📎 ${r.file}</p>`:""}
        <div class="muted" style="font-size:.74rem;margin-top:.2rem">${r.time}</div>
      </div>`).join("");
  } else {
    reviewsCard.style.display="none";
  }
}

function deleteMyLoad(i){
  if(!confirm("Удалить этот груз из ленты?"))return;
  const load=myAddedLoads[i];
  const loadsIdx=loads.indexOf(load);if(loadsIdx>-1)loads.splice(loadsIdx,1);
  myAddedLoads.splice(i,1);filterLoads();renderProfile();showToast("Груз удалён","success");
}
function openEditLoad(i){
  const l=myAddedLoads[i];
  document.getElementById("editLoadIdx").value=i;
  document.getElementById("editLoadFrom").value=l.from;
  document.getElementById("editLoadTo").value=l.to;
  document.getElementById("editLoadCargo").value=l.cargo;
  document.getElementById("editLoadWeight").value=parseFloat(l.weight);
  document.getElementById("editLoadPrice").value=l.price;
  document.getElementById("editLoadCompany").value=l.company||"";
  document.getElementById("editLoadModal").classList.add("open");
}
function saveEditLoad(){
  const i=parseInt(document.getElementById("editLoadIdx").value);
  const l=myAddedLoads[i];
  l.from=document.getElementById("editLoadFrom").value.trim()||l.from;
  l.to=document.getElementById("editLoadTo").value.trim()||l.to;
  l.cargo=document.getElementById("editLoadCargo").value.trim()||l.cargo;
  const w=document.getElementById("editLoadWeight").value;if(w)l.weight=`${w} т`;
  const p=document.getElementById("editLoadPrice").value;if(p)l.price=parseFloat(p);
  l.company=document.getElementById("editLoadCompany").value.trim();
  document.getElementById("editLoadModal").classList.remove("open");
  filterLoads();renderProfile();showToast("Груз обновлён","success");
}
function deleteMyTransport(i){
  if(!confirm("Удалить этот транспорт из поиска?"))return;
  const tr=myAddedTransports[i];
  const tIdx=transports.indexOf(tr);if(tIdx>-1)transports.splice(tIdx,1);
  myAddedTransports.splice(i,1);renderTransports(transports);renderProfile();showToast("Транспорт удалён","success");
}
function openEditTransport(i){
  const tr=myAddedTransports[i];
  document.getElementById("editTransportIdx").value=i;
  document.getElementById("editTransportName").value=tr.name;
  document.getElementById("editTransportModel").value=tr.model;
  document.getElementById("editTransportCap").value=tr.cap;
  document.getElementById("editTransportCity").value=tr.city;
  document.getElementById("editTransportRoutes").value=tr.routes||"";
  document.getElementById("editTransportModal").classList.add("open");
}
function saveEditTransport(){
  const i=parseInt(document.getElementById("editTransportIdx").value);
  const tr=myAddedTransports[i];
  tr.name=document.getElementById("editTransportName").value.trim()||tr.name;
  tr.model=document.getElementById("editTransportModel").value.trim()||tr.model;
  const c=document.getElementById("editTransportCap").value;if(c)tr.cap=parseFloat(c);
  tr.city=document.getElementById("editTransportCity").value.trim()||tr.city;
  tr.routes=document.getElementById("editTransportRoutes").value.trim();
  document.getElementById("editTransportModal").classList.remove("open");
  renderTransports(transports);renderProfile();showToast("Транспорт обновлён","success");
}


let brokerWalletBalance=0,brokerDealsCompleted=0,brokerTransactions=[],brokerContactRequests=[];
function brokerLogin(){
  if(currentUser?.role==="broker"){
    document.getElementById("brokerPanelGuest").style.display="none";
    document.getElementById("brokerPanelUser").style.display="block";
    renderBrokerPanel();return;
  }
  const loginRaw=document.getElementById("brokerLoginInput").value.trim();
  const pwd=document.getElementById("brokerPwdInput").value;
  const normalize=s=>s.replace(/\D/g,"").slice(-10);
  const ok=normalize(loginRaw)===normalize(MAIN_BROKER.contact)&&pwd===MAIN_BROKER.pwd;
  const err=document.getElementById("brokerLoginError");
  if(!ok){err.style.display="block";return;}
  err.style.display="none";
  document.getElementById("brokerPanelGuest").style.display="none";
  document.getElementById("brokerPanelUser").style.display="block";
  renderBrokerPanel();showToast(`Добро пожаловать, ${MAIN_BROKER.name} ${MAIN_BROKER.surname}!`,"success");
}
function updateBrokerAccessUI(){
  const brokerNav=document.getElementById("brokerNavBtn");
  const isBroker=currentUser?.role==="broker";
  if(isBroker){
    brokerNav.style.cssText="display:flex!important;background:rgba(124,58,237,.08);color:#4f46e5;border-color:rgba(124,58,237,.3)";
    document.getElementById("brokerPanelGuest").style.display="none";
    document.getElementById("brokerPanelUser").style.display="block";
    renderBrokerPanel();return;
  }
  brokerNav.style.display="none";
  document.getElementById("brokerPanelGuest").style.display="block";
  document.getElementById("brokerPanelUser").style.display="none";
}
function refreshChatRoleUI(){
  const isBroker=currentUser?.role==="broker";
  document.getElementById("confirmDeliveryBtn").style.display=isBroker?"none":"";
  document.getElementById("confirmReceiptBtn").style.display=isBroker?"none":"";
}
function renderBrokerPanel(){
  document.getElementById("brokerWalletBalance").textContent=fmt(brokerWalletBalance);
  document.getElementById("brokerDealsCount").textContent=brokerDealsCompleted;
  document.getElementById("brokerPendingCount").textContent=
    brokerContactRequests.filter(r=>r.status==="pending").length+
    pendingDeposits.filter(r=>r.status==="pending").length+
    pendingWithdrawals.filter(r=>r.status==="pending").length;
  document.getElementById("brokerEarnedTotal").textContent=fmt(brokerTransactions.reduce((s,t)=>s+t.amount,0));

  const supEl=document.getElementById("brokerSupportList");
  const pendingSup=supportMessages.filter(m=>m.status==="pending");
  document.getElementById("brokerSupportCount").textContent=`${pendingSup.length} новых`;
  supEl.innerHTML=supportMessages.length?supportMessages.map(m=>`
    <div class="broker-request-card">
      <div class="req-route">${m.from} · ${m.time}</div>
      <div class="req-meta">${m.text}${m.file?` · 📎 ${m.file}`:""}</div>
      ${m.status==="pending"?`<div class="broker-actions">
        <input type="text" id="supReply_${m.id}" placeholder="Ответ..." style="font-size:.82rem;padding:.35rem .6rem;border-radius:8px;border:1px solid var(--border);flex:1;min-width:150px;font-family:'Nunito',sans-serif">
        <button class="btn accent sm" onclick="sendSupportReply(${m.id})">Ответить</button>
      </div>`:`<div style="font-size:.8rem;color:#0b7a5f;margin-top:.3rem">✓ Отвечено: ${m.reply||""}</div>`}
    </div>`).join(""):`<p class="muted" style="text-align:center;padding:1rem">Сообщений нет</p>`;

  const rqEl=document.getElementById("brokerContactRequests");
  rqEl.innerHTML=brokerContactRequests.length?brokerContactRequests.map(r=>`
    <div class="broker-request-card">
      <div class="req-route">${r.route}</div>
      <div class="req-meta">Запрос от: <strong>${r.requester}</strong> · ${r.requesterPhone} · ${r.time}</div>
      <div class="req-meta">Компания: <strong>${r.company||"н/д"}</strong> · Владелец: <strong>${r.ownerPhone||"н/д"}</strong></div>
      <div class="req-meta">Статус: <span class="tc-badge ${r.status==="pending"?"badge-gold":r.status==="approved"?"badge-green":"badge-blue"}">${r.status==="pending"?"Ожидает":r.status==="approved"?"Одобрено":"Отклонено"}</span></div>
      ${r.status==="pending"?`<div class="broker-actions">
        <button class="btn accent sm" onclick="approveBrokerRequest(${r.id})">✓ Одобрить</button>
        <button class="btn ghost sm" onclick="rejectBrokerRequest(${r.id})">✕ Отклонить</button>
      </div>`:""}
    </div>`).join(""):`<p class="muted" style="text-align:center;padding:1rem">Запросов пока нет</p>`;

  const depEl=document.getElementById("brokerDepositsList");
  depEl.innerHTML=pendingDeposits.length?pendingDeposits.map(d=>`
    <div class="tx-item">
      <span>${d.user} · ${fmt(d.amount)} · к зачислению: ${fmt(d.net)}</span>
      <span style="display:flex;gap:.4rem;flex-wrap:wrap">
        ${d.status==="pending"?`<button class="btn accent sm" onclick="approveDeposit(${d.id})">✓</button><button class="btn ghost sm" onclick="rejectDeposit(${d.id})">✕</button>`:`<span class="tc-badge ${d.status==="approved"?"badge-green":"badge-blue"}">${d.status==="approved"?"Одобрено":"Отклонено"}</span>`}
      </span>
    </div>`).join(""):`<p class="muted" style="text-align:center;padding:1rem">Заявок нет</p>`;

  const wdEl=document.getElementById("brokerWithdrawalsList");
  wdEl.innerHTML=pendingWithdrawals.length?pendingWithdrawals.map(w=>`
    <div class="tx-item">
      <span>${w.user} · ${fmt(w.amount)} · ${w.firstName||""} ${w.lastName||""}</span>
      <span style="display:flex;gap:.4rem;flex-wrap:wrap">
        ${w.status==="pending"?`<button class="btn accent sm" onclick="approveWithdrawal(${w.id})">✓</button><button class="btn ghost sm" onclick="rejectWithdrawal(${w.id})">✕</button>`:`<span class="tc-badge ${w.status==="approved"?"badge-green":"badge-blue"}">${w.status==="approved"?"Одобрено":"Отклонено"}</span>`}
      </span>
    </div>`).join(""):`<p class="muted" style="text-align:center;padding:1rem">Заявок нет</p>`;

  const dlEl=document.getElementById("brokerDealsList");
  dlEl.innerHTML=activeDeals.length?activeDeals.map(d=>`
    <div class="deal-card">
      <div class="deal-info">
        <strong>${d.route}</strong>
        <span>${d.cargo} · Фрахт: ${fmt(d.price)} · Комиссия: ${fmt(d.commission)}</span>
        <span style="font-size:.78rem;color:var(--muted)">${d.time}</span>
      </div>
      <div class="deal-actions">
        <span class="tc-badge ${d.status==="active"?"badge-green":"badge-blue"}">${d.status==="active"?"В процессе":"Завершено"}</span>
        <button class="btn ghost sm" onclick="selectBrokerChat(${d.chatId||0})">Открыть чат</button>
      </div>
    </div>`).join(""):`<p class="muted" style="text-align:center;padding:1rem">Активных сделок нет</p>`;

  renderBrokerChatList();

  const txEl=document.getElementById("brokerTxList");
  txEl.innerHTML=brokerTransactions.length?brokerTransactions.map(tx=>`
    <div class="tx-item">
      <span>${tx.text}</span>
      <span class="tx-plus">+${fmt(tx.amount)}</span>
      <span class="muted" style="font-size:.78rem">${tx.date}</span>
    </div>`).join(""):`<p class="muted" style="text-align:center;padding:1rem">Транзакций нет</p>`;
}
function approveDeposit(id){
  const d=pendingDeposits.find(x=>x.id===id);if(!d)return;
  d.status="approved";
  if(currentUser&&currentUser.phone===d.phone){
    walletBalance+=d.net;
    transactions.unshift({type:"deposit",text:`Пополнение одобрено (${d.bank}), удержано 5%`,amount:+d.net,date:nowTime()});
  }
  brokerWalletBalance+=d.fee;
  brokerTransactions.unshift({text:`Комиссия 5% за пополнение (${d.user})`,amount:d.fee,date:nowTime()});
  renderWallet();renderBrokerPanel();
}
function rejectDeposit(id){const d=pendingDeposits.find(x=>x.id===id);if(d)d.status="rejected";renderBrokerPanel();}
function approveWithdrawal(id){
  const w=pendingWithdrawals.find(x=>x.id===id);if(!w)return;
  w.status="approved";
  if(currentUser&&currentUser.phone===w.phone){
    walletBalance-=w.amount;
    transactions.unshift({type:"withdraw",text:`Вывод одобрен (${w.bank})`,amount:-w.amount,date:nowTime()});
  }
  renderWallet();renderBrokerPanel();
}
function rejectWithdrawal(id){const w=pendingWithdrawals.find(x=>x.id===id);if(w)w.status="rejected";renderBrokerPanel();}
function approveBrokerRequest(id){
  const r=brokerContactRequests.find(x=>x.id===id);
  if(r){
    r.status="approved";
    const chat=chats.find(c=>c.route===r.route);
    if(chat)chat.messages.push({from:"broker-msg",text:`Запрос на контакты одобрен. Компания: ${r.company} · Телефон: ${r.ownerPhone}`,time:nowTime()});
    if(brokerActiveChatId&&chat&&chat.id===brokerActiveChatId)renderBrokerChatMessages();
  }
  renderBrokerPanel();showToast("Контакты раскрыты участникам сделки","success");
}
function rejectBrokerRequest(id){
  const r=brokerContactRequests.find(x=>x.id===id);if(r)r.status="rejected";renderBrokerPanel();showToast("Запрос отклонён","warn");
}


function toggleSupportPanel(){
  supportPanelOpen=!supportPanelOpen;
  document.getElementById("supportPanel").classList.toggle("open",supportPanelOpen);
  if(supportPanelOpen){supportUnread=0;updateSupportBadge();renderSupportChat();}
}
function switchSupportTab(tab){
  supportActiveTab=tab;
  document.getElementById("guideTab").classList.toggle("active",tab==="guide");
  document.getElementById("supportChatTabBtn").classList.toggle("active",tab==="support");
  document.getElementById("guidePanelContent").style.display=tab==="guide"?"block":"none";
  document.getElementById("supportChatContent").style.display=tab==="support"?"flex":"none";
  if(tab==="support"){renderSupportChat();}
}
function toggleArticle(header){
  const body=header.nextElementSibling;
  body.classList.toggle("open");
  header.querySelector("span").textContent=body.classList.contains("open")?"▴":"▾";
}
function updateSupportBadge(){
  const badge=document.getElementById("supportBadge");
  if(supportUnread>0){badge.textContent=supportUnread>9?"9+":supportUnread;badge.classList.add("show");}
  else badge.classList.remove("show");
}
function renderSupportChat(){
  const el=document.getElementById("supportChatMsgs");
  if(!supportMessages.length){
    el.innerHTML=`<div class="support-chat-empty"><div class="sce-icon">💬</div><p>Нет сообщений</p><p style="font-size:.78rem;margin-top:.25rem">Тут будут отображаться вопросы / жалобы</p></div>`;
    return;
  }
  el.innerHTML=supportMessages.map(m=>`
    <div class="supmsg ${m.isUser?"mine":"reply"}">
      ${m.isUser?"":`<div style="font-size:.69rem;font-weight:700;color:var(--violet);margin-bottom:.15rem">Поддержка Nurtay</div>`}
      ${m.text}${m.file?`<div style="font-size:.72rem;margin-top:.15rem;opacity:.8">📎 ${m.file}</div>`:""}
      <div class="supmsg-meta">${m.time}</div>
    </div>`).join("");
  el.scrollTop=el.scrollHeight;
}
function sendSupportMsg(){
  const inp=document.getElementById("supportChatInput");
  const text=inp.value.trim();if(!text)return;
  const from=currentUser?`${currentUser.name} ${currentUser.surname||""}`.trim():"Гость";
  const msg={id:Date.now(),from,text,time:nowTime(),status:"pending",isUser:true};
  supportMessages.push(msg);
  inp.value="";renderSupportChat();renderBrokerPanel();
  setTimeout(()=>{
    const autoReply={id:Date.now(),from:"Поддержка",text:"Ваш запрос получен. Наш специалист ответит в ближайшее время.",time:nowTime(),status:"replied",isUser:false};
    supportMessages.push(autoReply);
    if(supportPanelOpen&&supportActiveTab==="support"){renderSupportChat();}
    else{supportUnread++;updateSupportBadge();}
  },1800);
}
function attachSupportFile(input){
  const f=input.files?.[0];if(!f)return;
  const from=currentUser?`${currentUser.name} ${currentUser.surname||""}`.trim():"Гость";
  supportMessages.push({id:Date.now(),from,text:`📎 Файл отправлен`,file:f.name,time:nowTime(),status:"pending",isUser:true});
  renderSupportChat();input.value="";
}
function sendSupportReply(msgId){
  const replyEl=document.getElementById(`supReply_${msgId}`);if(!replyEl)return;
  const text=replyEl.value.trim();if(!text){showToast("Введите ответ","error");return;}
  const msg=supportMessages.find(m=>m.id===msgId);if(msg){msg.status="replied";msg.reply=text;}
  const replyMsg={id:Date.now(),from:"Поддержка",text,time:nowTime(),status:"replied",isUser:false};
  supportMessages.push(replyMsg);
  supportUnread++;updateSupportBadge();
  renderBrokerPanel();showToast("Ответ отправлен","success");
}


function adminLogin(){
  const pwd=document.getElementById("adminPwdInput").value;
  const err=document.getElementById("adminLoginError");
  if(pwd!==ADMIN_PWD){err.style.display="block";return;}
  err.style.display="none";
  document.getElementById("adminGuest").style.display="none";
  document.getElementById("adminPanelUser").style.display="block";
  renderAdminPanel();showToast("Добро пожаловать, Администратор!","success");
}
function updateAdminAccessUI(){}
function renderAdminPanel(){
  const users=JSON.parse(localStorage.getItem("nurtay_users")||"[]");
  document.getElementById("adminUsersCount").textContent=users.length;
  document.getElementById("adminDeletedCount").textContent=adminDeletedCount;

  const allNames=[...users.map(u=>`${u.name} ${u.surname||""}`.trim()),...transports.map(t=>t.name)];
  const uniqueNames=[...new Set(allNames)];
  const flagged=uniqueNames.filter(name=>{
    const avg=parseFloat(getAvgRating(name)||5);
    const warns=userWarnings[name]?.count||0;
    return avg<=2.5||(warns>=2&&userRatings[name]?.count>0);
  });
  document.getElementById("adminFlaggedCount").textContent=flagged.length;
  const totalWarns=Object.values(userWarnings).reduce((s,w)=>s+(w.count||0),0);
  document.getElementById("adminWarnCount").textContent=totalWarns;

  const notifEl=document.getElementById("adminNotifList");
  notifEl.innerHTML=adminNotifications.length?adminNotifications.slice().reverse().map(n=>`
    <div class="admin-notif">
      ${n.type==="lowRating"?`⭐ <strong>${n.name}</strong> получил низкий рейтинг: ${n.avg} — требуется проверка. <em>${n.time}</em>`:
        n.type==="3warnings"?`🚨 <strong>${n.name}</strong> получил 3/3 предупреждений! <em>${n.time}</em>`:
        `ℹ️ ${n.text||""} <em>${n.time}</em>`}
    </div>`).join(""):`<p class="muted" style="text-align:center;padding:.8rem">Нет уведомлений</p>`;

  const flaggedEl=document.getElementById("adminFlaggedList");
  if(!flagged.length){
    flaggedEl.innerHTML=`<p class="muted" style="text-align:center;padding:1rem">✅ Нет пользователей с плохим рейтингом</p>`;
  } else {
    flaggedEl.innerHTML=flagged.map(name=>{
      const avg=getAvgRating(name)||"нет оценок";
      const warns=userWarnings[name]?.count||0;
      const reviews=userRatings[name]?.reviews||[];
      const isDanger=parseFloat(avg)<=1.5||warns>=3;
      const isWarn=parseFloat(avg)<=2.5||warns>=2;
      return`<div class="admin-user-card ${isDanger?"danger-user":isWarn?"warn-user":""}">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:.5rem">
          <div>
            <p style="font-weight:700;font-size:.92rem">${name}</p>
            <p style="font-size:.82rem;color:var(--muted)">Рейтинг: ${avg} · ${userRatings[name]?.count||0} отзывов</p>
            <div style="display:flex;align-items:center;gap:.3rem;margin-top:.2rem">
              <span style="font-size:.82rem">Предупреждения:</span>
              <div class="warn-pips">${[1,2,3].map(i=>`<div class="warn-pip ${warns>=i?"filled":""}"></div>`).join("")}</div>
              <span style="font-size:.78rem;color:${warns>=3?"var(--danger)":"var(--muted)"}">${warns}/3</span>
            </div>
          </div>
          <div style="display:flex;gap:.4rem;flex-wrap:wrap">
            <button class="btn warn sm" onclick="issueWarning('${name.replace(/'/g,"\\'")}')">⚠️ Предупреждение</button>
            <button class="btn danger sm" onclick="deleteUserFromAdmin('${name.replace(/'/g,"\\'")}')">🗑 Удалить</button>
          </div>
        </div>
        ${reviews.length?`<div style="margin-top:.6rem;display:flex;flex-direction:column;gap:.4rem">
          ${reviews.slice(0,3).map(r=>`<div class="review-card" style="font-size:.8rem">
            <div class="rev-head"><span>${r.from}</span><span style="color:#f59e0b">${"★".repeat(r.rating)}${"☆".repeat(5-r.rating)}</span></div>
            ${r.comment?`<p>${r.comment}</p>`:""}
            ${r.file?`<p style="font-size:.74rem;color:var(--muted)">📎 ${r.file}</p>`:""}
          </div>`).join("")}
        </div>`:""}
      </div>`;
    }).join("");
  }

  const allUsersEl=document.getElementById("adminAllUsers");
  allUsersEl.innerHTML=users.length?users.map(u=>{
    const fullName=`${u.name} ${u.surname||""}`.trim();
    const avg=getAvgRating(fullName);
    const warns=userWarnings[fullName]?.count||0;
    const roleLabel={shipper:"Грузоотправитель",carrier:"Водитель",broker:"Брокер",admin:"Администратор"}[u.role]||u.role;
    return`<div class="admin-user-card">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.5rem">
        <div>
          <p style="font-weight:700;font-size:.9rem">${fullName}</p>
          <p style="font-size:.8rem;color:var(--muted)">${u.phone} · ${roleLabel}</p>
          ${avg?`<div>${renderStarsDisplay(avg)}</div>`:"<div style='font-size:.78rem;color:var(--muted)'>Нет отзывов</div>"}
          ${warns>0?`<div class="tc-badge badge-red" style="margin-top:.2rem">⚠️ ${warns}/3 предупреждений</div>`:""}
        </div>
        <div style="display:flex;gap:.4rem;flex-wrap:wrap">
          <button class="btn warn sm" onclick="issueWarning('${fullName.replace(/'/g,"\\'")}')">⚠️ Пред.</button>
          <button class="btn danger sm" onclick="deleteUserFromAdmin('${fullName.replace(/'/g,"\\'")}')" style="font-size:.76rem">🗑 Удалить</button>
        </div>
      </div>
    </div>`;
  }).join(""):`<p class="muted" style="text-align:center;padding:1rem">Пользователей нет</p>`;
}
function issueWarning(name){
  if(!userWarnings[name])userWarnings[name]={count:0};
  userWarnings[name].count=Math.min(userWarnings[name].count+1,3);
  const warns=userWarnings[name].count;
  if(warns>=3){
    adminNotifications.push({type:"3warnings",name,time:nowTime()});
    showToast(`⚠️ ${name} получил 3/3 предупреждений!`,"error");
  } else {
    showToast(`Предупреждение выдано: ${name} (${warns}/3)`,"warn");
  }
  renderAdminPanel();renderTransports(transports);
}
function deleteUserFromAdmin(name){
  if(!confirm(`Удалить пользователя ${name}? Это действие необратимо.`))return;
  const users=JSON.parse(localStorage.getItem("nurtay_users")||"[]");
  const filtered=users.filter(u=>`${u.name} ${u.surname||""}`.trim()!==name);
  localStorage.setItem("nurtay_users",JSON.stringify(filtered));
  adminDeletedCount++;
  showToast(`Пользователь ${name} удалён`,"success");
  renderAdminPanel();
}


document.addEventListener("keydown",e=>{
  if(e.key==="Escape"){
    ["authModal","respondModal","distModal","walletModal","loadOfferModal","transportOrderModal","chatModal","editLoadModal","editTransportModal","profileEditModal","ratingModal"].forEach(id=>{
      const el=document.getElementById(id);if(el)el.classList.remove("open");
    });
    if(supportPanelOpen){supportPanelOpen=false;document.getElementById("supportPanel").classList.remove("open");}
  }
});
document.getElementById("distModal").addEventListener("click",e=>{if(e.target.id==="distModal")document.getElementById("distModal").classList.remove("open");});


function init(){
  fillSelect("fromCity",cities);
  fillSelect("toCity",cities);
  fillSelect("tc-fromCity",cities);
  const cityArr=["—Выберите город—",...Array.from(citySet).sort((a,b)=>a.localeCompare(b,"ru"))];
  fillSelect("al-from",cityArr);
  fillSelect("al-to",cityArr);
  fillBodySelect("bodyType");
  fillBodySelect("tc-body");
  fillBodySelect("al-body");
  fillBodySelect("at-body");
  initDate();
  filterLoads();
  filterTransports();
  renderProfile();
  initRatingStars();
  // ✅ Admin nav button — violet style
  document.getElementById("adminNavBtn").style.cssText="display:flex!important;background:rgba(124,58,237,.08);color:#4f46e5;border-color:rgba(124,58,237,.3)";
  const saved=localStorage.getItem("nurtay_session");
  if(saved){
    try{const u=JSON.parse(saved);setUser(u);renderProfile();}catch(e){}
  }
  updateBrokerAccessUI();
  renderChatMessages();
}

init();
</script>
</body>
</html>
