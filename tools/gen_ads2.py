import json
exec(open('gen_ads.py').read().split('ADS=[')[0])
ADS=[
 ('ad13-web-boutique','bg2/ad-boutique.jpg','','laptop',S+'lumi-01-hero.jpg','Customers google you first.','Does your website sell for you?','Bilingual company websites, phone-first, with enquiry forms that reach you — <b>designed, written and hosted on your own account.</b>','Built for','UAE businesses','See our work →'),
 ('ad14-vat-return','bg2/ad-accdesk.jpg','','tablet',S+'wealth-10-vat-return.jpg','VAT return due Thursday?','Ready by Monday.','Sales, purchases and expenses posted as they happen — the return builds itself, and <b>every figure links back to its invoice.</b>','Built for','UAE VAT · AED','See the accounts demo →'),
 ('ad15-geofence','bg2/ad-sitenight.jpg','','phone',S+'uec-g1-choose-site.jpg','Clock-in only works','inside the site fence.','GPS geofence on the worker’s own phone — <b>no buddy punching, no paper sheets, no extra hardware.</b>','Built for','contractors &amp; MEP','Try the live demo →'),
 ('ad16-utilization','bg2/ad-cabin.jpg','','laptop',S+'uec-15-utilization.jpg','Which projects eat your hours?','Know by Friday.','Hours by worker, site and project roll up on their own — <b>utilisation and cost per project, every week, not at year end.</b>','Built for','project companies','Try the live demo →'),
 ('ad17-learning','bg2/ad-library.jpg','','phone',P+'learn-m01-practice.jpg','Practice questions','in every student’s pocket.','Chapters, short notes and self-marking quizzes — <b>your school’s own app, with your name on it.</b>','Built for','schools &amp; academies','Ask for a demo →'),
 ('ad18-project-pl','bg2/ad-harbour.jpg','','laptop',S+'ewp-15-pl.jpg','Profit by project,','not just profit by year.','Every invoice, cost and timesheet tagged to its project — <b>see which jobs make money while you can still act.</b>','Built for','consultancies','Try the live demo →'),
 ('ad19-parents-ar','bg2/ad-nurseryrecep.jpg','ar','phone',S+'cka-14-arabic-policy-signing.jpg','أولياء الأمور يوقّعون','السياسات من الجوال.','تصل سياسات الحضانة ونماذجها لكل وليّ أمر بالعربية أو الإنجليزية، ويوقّعها بإصبعه — <b>بدون ورق، ومع سجلّ كامل لكل توقيع.</b>','','الحضانات · EYFS','جرّب العرض التجريبي ←'),
 ('ad20-md-week','bg2/ad-boardroom.jpg','','laptop',S+'ewp-18-md.jpg','The MD’s Monday question:','What needs me this week?','Pipeline, cash, late reports and open risks on one page — <b>updated by the team, read in two minutes.</b>','Built for','managing directors','Try the live demo →'),
 ('ad21-cheques','bg2/ad-study.jpg','','tablet',S+'wealth-07-cheques.jpg','Post-dated cheques,','no more surprises.','Every cheque in and out, by company and bank, with a reminder before it is due — <b>private, on your own server.</b>','Built for','private offices','Ask for a private demo →'),
 ('ad22-billed-hours','bg2/ad-mepyard.jpg','','laptop',S+'uec-09-sales-overview.jpg','Every hour your team worked —','billed?','Timesheets turn into client invoices in a click — <b>no missed hours, no month-end catch-up.</b>','Built for','manpower &amp; MEP','Try the live demo →'),
]
man=[]
for n,bg,cls,kind,shot,small,big,sub,pl,pb,cta in ADS:
    pill=f'<div class="pill">{pl} <b>{pb}</b></div>' if pl else f'<div class="pill"><b>{pb}</b></div>'
    site='global-link.ae' if 'website' in sub or 'school' in sub or 'private' in sub else 'demo.global-link.ae'
    html=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{cls}"><img class="bg" src="{bg}"><div class="gt"></div><div class="gb"></div><div class="stage">{dev(kind,shot)}</div><div class="h"><small>{small}</small>{big}</div><div class="s">{sub}</div>{pill}<div class="cta">{cta}</div><div class="brand"><img src="{LOGO}">Global Link</div><div class="site">{site}</div></body></html>'
    open(n+'.html','w').write(html); man.append([n,1080,1350])
json.dump(man,open('manifest-ad4.json','w')); print(len(man))
