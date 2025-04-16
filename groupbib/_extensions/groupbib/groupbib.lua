
-- Reformat all heading text 
function Header(el)
  el.content = pandoc.Emph(el.content)
  return el
end

-- Group references by type
function Div(el)
  if el.classes:includes('references') then
      local in_press = {}
      local preprints = {}
      local others = {}

      for _, item in ipairs(el.content) do
          local text = pandoc.utils.stringify(item)
          if text:match("in-press") then
              table.insert(in_press, item)
          elseif text:match("preprint") then
              table.insert(preprints, item)
          else
              table.insert(others, item)
          end
      end

      local grouped = {}

      if #in_press > 0 then
          table.insert(grouped, pandoc.RawBlock('markdown', '### In Press'))
          for _, item in ipairs(in_press) do
              table.insert(grouped, item)
          end
      end

      if #preprints > 0 then
          table.insert(grouped, pandoc.RawBlock('markdown', '### Preprints'))
          for _, item in ipairs(preprints) do
              table.insert(grouped, item)
          end
      end

      if #others > 0 then
          table.insert(grouped, pandoc.RawBlock('markdown', '### Other Publications'))
          for _, item in ipairs(others) do
              table.insert(grouped, item)
          end
      end

      el.content = grouped
      return el
  end
end