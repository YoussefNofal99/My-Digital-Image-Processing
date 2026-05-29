const OPERATIONS = [
  {
    category: 'Point Operations',
    opt: [
      { id: 'add',         name: 'Add Brightness',
        para: [{ id:'num', label:'Amount', type:'range', min:0, max:255, step:1, def:50 }] },
      { id: 'subtract',    name: 'Subtract Brightness',
        para: [{ id:'num', label:'Amount', type:'range', min:0, max:255, step:1, def:50 }] },
      { id: 'multiply',    name: 'Multiply',
        para: [{ id:'num', label:'Factor', type:'range', min:0.1, max:5, step:0.1, def:1.5 }] },
      { id: 'divide',      name: 'Divide',
        para: [{ id:'num', label:'Divisor', type:'range', min:0.1, max:5, step:0.1, def:1.5 }] },
      { id: 'complement',  name: 'Complement (Invert)', para: [] },
    ]
  },
    {
    category: 'Image Operations',
    opt: [
      { id: 'addimg',      name: 'Add Two Images',      para: [], needsImg2: true },
      { id: 'subtractimg', name: 'Subtract Two Images', para: [], needsImg2: true },
      { id: 'multiplyimg', name: 'Multiply Two Images', para: [], needsImg2: true },
      { id: 'divideimg',   name: 'Divide Two Images',   para: [], needsImg2: true },
    ]
  },
  {
    category: 'Color Operations',
    opt: [
      { id: 'change',    name: 'Set Channel Value',
        para: [
          { id:'num', label:'Value', type:'range', min:0, max:255, step:1, def:50 },
          { id:'i',   label:'Channel', type:'select',
            options:[{v:0,l:'Red'},{v:1,l:'Green'},{v:2,l:'Blue'}], def:0 }
        ]},
      { id: 'swap',     name: 'Swap Two Channels',
        para: [
          { id:'i', label:'Channel A', type:'select',
            options:[{v:0,l:'Red'},{v:1,l:'Green'},{v:2,l:'Blue'}], def:0 },
          { id:'j', label:'Channel B', type:'select',
            options:[{v:0,l:'Red'},{v:1,l:'Green'},{v:2,l:'Blue'}], def:1 }
        ]},
      { id: 'eliminate', name: 'Eliminate Channel',
        para: [
          { id:'i', label:'Channel', type:'select',
            options:[{v:0,l:'Red'},{v:1,l:'Green'},{v:2,l:'Blue'}], def:0 }
        ]},
    ]
  },
  {
    category: 'Histogram',
    opt: [
      { id: 'histstretch',  name: 'Histogram Stretching',
        para: [{ id:'gray', label:'Grayscale Mode', type:'toggle', def:true }] },
      { id: 'histequalization', name: 'Histogram Equalization',
        para: [{ id:'gray', label:'Grayscale Mode', type:'toggle', def:true }] },
    ]
  },
  {
    category: 'Edge Detection',
    opt: [
      { id: 'sobel', name: 'Sobel Edge Detector',
        para: [] },
      { id: 'prewitt', name: 'Prewitt Edge Detector',
        para: [] },
      { id: 'roberts', name: 'roberts Edge Detector',
        para: [] },
    ]
  },
  {
    category: 'Salt And Pepper Noise & Restoration',
    opt: [
      { id: 'spadd', name: 'Add Salt & Pepper Noise', para: [
          { id:'sprop', label:'Salt probability', type:'range', min:0, max:1, step:0.01, def:0.1 },
          { id:'pprop', label:'Pepper probability',  type:'range', min:0, max:1, step:0.01, def:0.1 },
      ] },
      { id: 'outlier',   name: 'Outlier Filter',
        para: [
          { id:'th', label:'Threshold', type:'range', min:5, max:100, step:1, def:30 },
          { id:'x',  label:'Kernel Width',  type:'range', min:1, max:15, def:3 },
          { id:'y',  label:'Kernel Height', type:'range', min:1, max:15, def:3 },
          { id:'add',   label:'Add Noise First',  type:'toggle', def:false },
          { id:'sprop', label:'Salt probability', type:'range',  min:0,  max:1,  step:0.01, def:0.1,  showIf:'add' },
          { id:'pprop', label:'Pepper probability',type:'range', min:0,  max:1,  step:0.01, def:0.1,  showIf:'add' },
        ]},
      { id: 'spmean',   name: 'Average Filter',
        para: [
          { id:'x', label:'Kernel Width',  type:'range', min:1, max:15, def:3 },
          { id:'y', label:'Kernel Height', type:'range', min:1, max:15, def:3 },
          { id:'add',   label:'Add Noise First',  type:'toggle', def:false },
          { id:'sprop', label:'Salt probability', type:'range',  min:0,  max:1,  step:0.01, def:0.1,  showIf:'add' },
          { id:'pprop', label:'Pepper probability',type:'range', min:0,  max:1,  step:0.01, def:0.1,  showIf:'add' },
        ]},
      { id: 'spmadian',    name: 'Median Filter',
        para: [
          { id:'x', label:'Kernel Size', type:'range', min:1, max:15, step:2, def:3 },
          { id:'add',   label:'Add Noise First',  type:'toggle', def:false },
          { id:'sprop', label:'Salt probability', type:'range',  min:0,  max:1,  step:0.01, def:0.1,  showIf:'add' },
          { id:'pprop', label:'Pepper probability',type:'range', min:0,  max:1,  step:0.01, def:0.1,  showIf:'add' },
        ] },
    ]
  },
  {
    category: 'Gaussian Noise & Restoration',
    opt: [
      { id: 'gadd', name: 'Add Gaussian Noise',
        para: [
          { id:'std',  label:'Standard Deviation', type:'range', min:1, max:80, step:1, def:15 },
          { id:'mean', label:'Mean',    type:'range', min:-50, max:50, step:1, def:0 },
        ]},
      { id: 'gmean',   name: 'Average Filter',
        para: [
          { id:'x', label:'Kernel Width',  type:'range', min:1, max:15, def:3 },
          { id:'y', label:'Kernel Height', type:'range', min:1, max:15, def:3 },
          { id:'add',   label:'Add Noise First',  type:'toggle', def:false },
          { id:'std',  label:'Standard Deviation', type:'range', min:1, max:80, step:1, def:15 , showIf:'add'},
          { id:'mean', label:'Mean',    type:'range', min:-50, max:50, step:1, def:0 , showIf:'add'},
        ]},
      { id: 'imageaverging', name: 'Image Averaging',
        para: [
          { id:'num', label:'Num Frames', type:'range', min:2, max:30, step:1, def:10 },
          { id:'std',  label:'Standard Deviation', type:'range', min:1, max:80, step:1, def:15 },
          { id:'mean', label:'Mean',    type:'range', min:-50, max:50, step:1, def:0 },
        ] },
    ]
  },
  {
    category: 'Image Segmentation',
    opt: [
      { id: 'gthr',   name: 'Global Thresholding',
        para: [{ id:'thr', label:'Threshold', type:'range', min:0, max:255, step:1, def:127 }] },
      { id: 'adathr', name: 'Adaptive Thresholding',
        para: [
          { id:'bsize', label:'Block Size', type:'range', min:3, max:51, step:2, def:11 },
          { id:'c',     label:'C Constant', type:'range', min:0, max:20, step:1, def:5 },
        ]},
      { id: 'autothr',     name: 'Auto (Isodata) Thresholding',
        para: [
          { id:'delta',  label:'Delta', type:'range', min:0.01, max:2, step:0.01, def:0.1 },
          { id:'maxi', label:'Max Iterations',  type:'range', min:10, max:500, step:10, def:100 },
        ]},
    ]
  },
  {
    category: 'Mathematical Morphology',
    opt: [
      { id: 'dilation', name: 'Dilation',
        para: [
          { id:'x', label:'Kernel Width',  type:'range', min:1, max:15, step:2, def:3 },
          { id:'y', label:'Kernel Height', type:'range', min:1, max:15, step:2, def:3 },
        ]},
      { id: 'erosion',  name: 'Erosion',
        para: [
          { id:'x', label:'Kernel Width',  type:'range', min:1, max:15, step:2, def:3 },
          { id:'y', label:'Kernel Height', type:'range', min:1, max:15, step:2, def:3 },
        ]},
      { id: 'opening',  name: 'Opening',
        para: [
          { id:'x', label:'Kernel Width',  type:'range', min:1, max:15, step:2, def:3 },
          { id:'y', label:'Kernel Height', type:'range', min:1, max:15, step:2, def:3 },
        ]},
      { id: 'closing',  name: 'Closing',
        para: [
          { id:'x', label:'Kernel Width',  type:'range', min:1, max:15, step:2, def:3 },
          { id:'y', label:'Kernel Height', type:'range', min:1, max:15, step:2, def:3 },
        ]},
      { id: 'gradient', name: 'Morphological Gradient',
        para: [
          { id:'x', label:'Kernel Width',  type:'range', min:1, max:15, step:2, def:3 },
          { id:'y', label:'Kernel Height', type:'range', min:1, max:15, step:2, def:3 },
        ]},
      { id: 'external', name: 'External Boundary',
        para: [
          { id:'x', label:'Kernel Width',  type:'range', min:1, max:15, step:2, def:3 },
          { id:'y', label:'Kernel Height', type:'range', min:1, max:15, step:2, def:3 },
        ]},
      { id: 'internal', name: 'Internal Boundary',
        para: [
          { id:'x', label:'Kernel Width',  type:'range', min:1, max:15, step:2, def:3 },
          { id:'y', label:'Kernel Height', type:'range', min:1, max:15, step:2, def:3 },
        ]},
    ]
  },
  {
    category: 'Linear Filters',
    opt: [
      { id: 'mean',    name: 'Average Filter',
        para: [
          { id:'x', label:'Kernel Width',  type:'range', min:1, max:15, def:3 },
          { id:'y', label:'Kernel Height', type:'range', min:1, max:15, def:3 },
        ]},
      { id: 'laplacian',  name: 'Laplacian Filter',
        para: [{ id:'k', label:'4-Connectivity Kernel', type:'toggle', def:true }] },
    ]
  },
  {
    category: 'Non-Linear Filters',
    opt: [
      { id: 'median',  name: 'Median Filter',
        para: [{ id:'x', label:'Kernel Size', type:'range', min:1, max:15, step:2, def:3 }] },
      { id: 'max',     name: 'Max Filter',
        para: [
          { id:'x', label:'Kernel Width',  type:'range', min:1, max:11, def:3 },
          { id:'y', label:'Kernel Height', type:'range', min:1, max:11, def:3 },
        ]},
      { id: 'min',     name: 'Min Filter',
        para: [
          { id:'x', label:'Kernel Width',  type:'range', min:1, max:11, def:3 },
          { id:'y', label:'Kernel Height', type:'range', min:1, max:11, def:3 },
        ]},
      { id: 'mode',    name: 'Mode Filter',
        para: [
          { id:'x', label:'Kernel Width',  type:'range', min:1, max:7, def:3 },
          { id:'y', label:'Kernel Height', type:'range', min:1, max:7, def:3 },
        ]},
    ]
  },
];

let currentFile   = null;
let currentFile2  = null;
let currentOp     = null;
let resultDataUrl = null;
let originalDataUrl = null;
let histDataUrl     = null;
let compDataUrl     = null;

const uploadZone    = document.getElementById('upload-zone');
const uploadZone2   = document.getElementById('upload-zone-2');
const imgInput      = document.getElementById('image-input');
const imgInput2     = document.getElementById('image-input-2');
const uploadContent = document.getElementById('upload-content');
const uploadPreview = document.getElementById('upload-preview');
const uploadContent2 = document.getElementById('upload-content-2');
const uploadPreview2 = document.getElementById('upload-preview-2');
const secondSection = document.getElementById('second-image-section');
const optList       = document.getElementById('operations-list');
const paraSection = document.getElementById('para-section');
const paraGrid    = document.getElementById('para-grid');
const processBtn    = document.getElementById('process-btn');
const downloadBtn   = document.getElementById('download-btn');
const originalPane  = document.getElementById('original-pane');
const processedPane = document.getElementById('processed-pane');
const infoOp        = document.getElementById('info-op');
const infoStatus    = document.getElementById('info-status');
const loadingOverlay= document.getElementById('loading-overlay');
const downloadSubplotBtn = document.getElementById('download-subplot-btn');
const downloadHistBtn    = document.getElementById('download-hist-btn');

function buildOperationsList() {
  optList.innerHTML = '';
  OPERATIONS.forEach(group => {
    const cat = document.createElement('div');
    cat.className = 'op-category';

    const header = document.createElement('div');
    header.className = 'op-category-header';
    header.innerHTML = `<span class="op-cat-name">${group.category}</span><span class="op-cat-arrow">›</span>`;
    header.addEventListener('click', () => {
      const wasOpen = header.classList.contains('open');
      document.querySelectorAll('.op-category-header').forEach(h => h.classList.remove('open'));
      if (!wasOpen) header.classList.add('open');
    });

    const items = document.createElement('div');
    items.className = 'op-items';
    group.opt.forEach(op => {
      const item = document.createElement('div');
      item.className = 'op-item';
      item.dataset.id = op.id;
      item.textContent = op.name;
      item.addEventListener('click', () => selectOperation(op));
      items.appendChild(item);
    });

    cat.appendChild(header);
    cat.appendChild(items);
    optList.appendChild(cat);
  });
}

function selectOperation(op) {
  currentOp = op;

  document.querySelectorAll('.op-item').forEach(el => {
    el.classList.toggle('selected', el.dataset.id === op.id);
  });

  secondSection.style.display = op.needsImg2 ? 'block' : 'none';

  buildpara(op);

  infoOp.textContent = op.name;
  updateProcessBtn();
}

function handleFile(file, isSecond, preview, content) {
  if (isSecond) { currentFile2 = file; }
  else {
    currentFile = file;
    originalDataUrl = URL.createObjectURL(file);
    showOriginal(originalDataUrl);
  }

  const url = URL.createObjectURL(file);
  preview.src = url;
  preview.classList.remove('hidden');
  content.style.display = 'none';

  updateProcessBtn();
}

const PARAM_KERNELS = {
  laplacian: {
    k: (val) => val
      ? { title: 'Laplacian1', cols: 3, cells: [0,-1,0,-1,4,-1,0,-1,0] }
      : { title: 'Laplacian2', cols: 3, cells: [1,-2,1,-2,4,-2,1,-2,1] }
  }
};

function renderKernelTooltip(kernelDef) {
  const { title, cols, cells } = kernelDef;
  const rows = Math.ceil(cells.length / cols);
  let cellsHtml = cells.map(v => {
    const cls = v === 0 ? 'zero' : v > 0 ? 'pos' : 'neg';
    return `<div class="kernel-cell ${cls}">${v}</div>`;
  }).join('');
  return `
    <div class="kernel-tooltip" id="kernel-tip">
      <div class="kernel-tooltip-title">${title}</div>
      <div class="kernel-grid" style="grid-template-columns:repeat(${cols},32px)">
        ${cellsHtml}
      </div>
    </div>`;
}

function buildpara(op) {
  paraGrid.innerHTML = '';

  if (!op.para || op.para.length === 0) {
    paraSection.style.display = 'none';
    return;
  }

  op.para.forEach(p => {
    const row = document.createElement('div');
    row.className = 'param-row';
    row.dataset.paramId = p.id;

    if (p.showIf) {
      const controller = op.para.find(c => c.id === p.showIf);
      row.style.display = (controller && controller.def) ? 'flex' : 'none';
      row.style.flexDirection = 'column';
      row.style.gap = '0.3rem';
    }

    if (p.type === 'range') {
      row.innerHTML = `
        <label class="param-label">
          ${p.label}
          <span class="param-value" id="val-${p.id}">${p.def}</span>
        </label>
        <input type="range" id="param-${p.id}" min="${p.min}" max="${p.max}" step="${p.step || 1}" value="${p.def}" />
      `;
      row.querySelector(`#param-${p.id}`).addEventListener('input', e => {
        document.getElementById(`val-${p.id}`).textContent = e.target.value;
      });

    } else if (p.type === 'select') {
      const opts = p.options.map(o =>
        `<option value="${o.v}" ${o.v === p.def ? 'selected' : ''}>${o.l}</option>`
      ).join('');
      row.innerHTML = `
        <label class="param-label">${p.label}</label>
        <select id="param-${p.id}">${opts}</select>
      `;

  } else if (p.type === 'toggle') {
    const kernelFns = PARAM_KERNELS[currentOp?.id];
    const getKernel = kernelFns?.[p.id];

    row.innerHTML = `
      <div class="toggle-row">
        <span class="toggle-label">${p.label}</span>
        <label class="toggle">
          <input type="checkbox" id="param-${p.id}" ${p.def ? 'checked' : ''} />
          <div class="toggle-track"></div>
          <div class="toggle-thumb"></div>
        </label>
        ${getKernel ? renderKernelTooltip(getKernel(p.def)) : ''}
      </div>
    `;

    setTimeout(() => {
      const checkbox = document.getElementById(`param-${p.id}`);
      if (!checkbox) return;

      if (getKernel) {
        const toggleRow = checkbox.closest('.toggle-row');
        const tip = toggleRow?.querySelector('.kernel-tooltip');
        if (tip && toggleRow) {
          toggleRow.addEventListener('mouseenter', () => tip.classList.add('visible'));
          toggleRow.addEventListener('mouseleave', () => tip.classList.remove('visible'));

          checkbox.addEventListener('change', () => {
            const k = getKernel(checkbox.checked);
            tip.querySelector('.kernel-tooltip-title').textContent = k.title;
            const grid = tip.querySelector('.kernel-grid');
            grid.innerHTML = k.cells.map(v => {
              const cls = v === 0 ? 'zero' : v > 0 ? 'pos' : 'neg';
              return `<div class="kernel-cell ${cls}">${v}</div>`;
            }).join('');
          });
        }
      }

      checkbox.addEventListener('change', () => {
        op.para.forEach(dep => {
          if (dep.showIf === p.id) {
            const depRow = paraGrid.querySelector(`[data-param-id="${dep.id}"]`);
            if (depRow) {
              depRow.style.display = checkbox.checked ? 'flex' : 'none';
              depRow.style.flexDirection = 'column';
              depRow.style.gap = '0.3rem';
            }
          }
        });
      });
    }, 0);
  }

    paraGrid.appendChild(row);
  });

  paraSection.style.display = 'block';
}

function gatherpara() {
  const para = {};
  if (!currentOp || !currentOp.para) return para;
  currentOp.para.forEach(p => {
    const el = document.getElementById(`param-${p.id}`);
    if (!el) return;
    if (p.type === 'toggle') {
      para[p.id] = el.checked;
    } else if (p.type === 'range') {
      para[p.id] = parseFloat(el.value);
    } else if (p.type === 'select') {
      para[p.id] = parseInt(el.value);
    }
  });
  return para;
}

function setupUpload(zone, input, content, preview, isSecond) {
  zone.addEventListener('click', () => input.click());
  zone.addEventListener('dragover', e => { e.preventDefault(); zone.classList.add('drag-over'); });
  zone.addEventListener('dragleave', () => zone.classList.remove('drag-over'));
  zone.addEventListener('drop', e => {
    e.preventDefault(); zone.classList.remove('drag-over');
    const file = e.dataTransfer.files[0];
    if (file && file.type.startsWith('image/')) handleFile(file, isSecond, preview, content);
  });
  input.addEventListener('change', () => {
    if (input.files[0]) handleFile(input.files[0], isSecond, preview, content);
  });
}

function showOriginal(url) {
  originalPane.innerHTML = `<img src="${url}" alt="Original" />`;
}

function updateProcessBtn() {
  const ready = currentFile && currentOp &&
    (!currentOp.needsImg2 || currentFile2);
  processBtn.disabled = !ready;
}

function setStatus(state, text) {
  infoStatus.className = `status-dot ${state}`;
  infoStatus.textContent = `●  ${text}`;
}

processBtn.addEventListener('click', async () => {
  if (!currentFile || !currentOp) return;

  setStatus('processing', 'Processing…');
  loadingOverlay.classList.remove('hidden');
  processBtn.disabled = true;
  vid.play();

  const para = gatherpara();
  const formData = new FormData();
  formData.append('image', currentFile);
  formData.append('opt', currentOp.id);
  formData.append('para', JSON.stringify(para));
  if (currentFile2) formData.append('image2', currentFile2);

  let data = null;

  try {
    const res  = await fetch('/process', { method: 'POST', body: formData });
    data = await res.json();

    if (data.error) throw new Error(data.error);

    resultDataUrl = `data:image/png;base64,${data.image}`;
    processedPane.innerHTML = `<img src="${resultDataUrl}" alt="Processed" />`;
    
    if (data.comparison) {
        compDataUrl = `data:image/png;base64,${data.comparison}`;
    } else {
        compDataUrl = null;
    }

    downloadBtn.classList.remove('hidden');
    if (downloadSubplotBtn) downloadSubplotBtn.classList.remove('hidden');

    if (data.plot) {
        histDataUrl = `data:image/png;base64,${data.plot}`;
        if (downloadHistBtn) downloadHistBtn.classList.remove('hidden');
    } else {
        histDataUrl = null;
        if (downloadHistBtn) downloadHistBtn.classList.add('hidden');
    }

    setStatus('done', 'Done');
  } catch (err) {
    processedPane.innerHTML = `
      <div class="pane-placeholder">
        <p style="color:var(--error)">Error: ${err.message}</p>
      </div>`;
    setStatus('error', 'Error');
    compDataUrl = null;

    downloadBtn.classList.add('hidden');
    if (downloadSubplotBtn) downloadSubplotBtn.classList.add('hidden');
    if (downloadHistBtn) downloadHistBtn.classList.add('hidden');
  } finally {
    loadingOverlay.classList.add('hidden');
    updateProcessBtn();
    vid.pause();
  }
});

if (downloadSubplotBtn) {
  downloadSubplotBtn.addEventListener('click', () => {
    if (!compDataUrl) return;
    
    const a = document.createElement('a');
    a.href = compDataUrl;
    a.download = `imagelab_subplot_${currentOp ? currentOp.id : 'comparison'}.png`;
    a.click();
  });
}

if (downloadHistBtn) {
  downloadHistBtn.addEventListener('click', () => {
    if (!histDataUrl) return;
    const a = document.createElement('a');
    a.href = histDataUrl;
    a.download = `imagelab_histogram_${currentOp ? currentOp.id : 'plot'}.png`;
    a.click();
  });
}

downloadBtn.addEventListener('click', () => {
  if (!resultDataUrl) return;
  const a = document.createElement('a');
  a.href = resultDataUrl;
  a.download = `imagelab_${currentOp ? currentOp.id : 'result'}.png`;
  a.click();
});

setupUpload(uploadZone, imgInput, uploadContent, uploadPreview, false);
setupUpload(uploadZone2, imgInput2, uploadContent2, uploadPreview2, true);
buildOperationsList();

const vid = document.getElementById('sonic');
const running = document.querySelector('.running');
const spinner = document.querySelector('.spinner');

running.addEventListener('mouseenter', () => {
  vid.playbackRate = 1.5;
  spinner.style.animationDuration = '0.5s';
});
running.addEventListener('mouseleave', () => {
  vid.playbackRate = 1;
  spinner.style.animationDuration = '1s';
});


const themeToggle = document.getElementById('themeToggle');
const themeIcon   = document.getElementById('themeIcon');

const DARK_TORCH  = themeIcon.src;
const LIGHT_TORCH = DARK_TORCH.replace('Dark-Torch.gif', 'Torch.gif');

themeToggle.addEventListener('click', () => {
  const isLight = document.documentElement.classList.toggle('light-mode');
  themeIcon.src = isLight ? LIGHT_TORCH : DARK_TORCH;
  const hoverIcon = document.getElementById('hoverIcon');
  hoverIcon.src = isLight ? DARK_TORCH : LIGHT_TORCH;
});