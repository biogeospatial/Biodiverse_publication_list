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
  
        -- Debug: Print the entire content of the references div
        print("Processing references div...")
  
        -- Categorize references
        for _, item in ipairs(el.content) do
            local text = pandoc.utils.stringify(item)
            print("Reference text:", text) -- Debug: Print each reference text
            if text:match("in-press") then
                print("Categorized as: In Press") -- Debug
                table.insert(in_press, item)
            elseif text:match("preprint") then
                print("Categorized as: Preprint") -- Debug
                table.insert(preprints, item)
            else
                print("Categorized as: Other") -- Debug
                table.insert(others, item)
            end
        end
  
        -- Debug: Print counts of each category
        print("In Press count:", #in_press)
        print("Preprints count:", #preprints)
        print("Others count:", #others)
  
        -- Create grouped sections
        local grouped = {}
  
        if #in_press > 0 then
            table.insert(grouped, pandoc.RawBlock('markdown', '## In Press'))
            for _, item in ipairs(in_press) do
                table.insert(grouped, item)
            end
        end
  
        if #preprints > 0 then
            table.insert(grouped, pandoc.RawBlock('markdown', '## Preprints'))
            for _, item in ipairs(preprints) do
                table.insert(grouped, item)
            end
        end
  
        if #others > 0 then
            table.insert(grouped, pandoc.RawBlock('markdown', '## References'))
            for _, item in ipairs(others) do
                table.insert(grouped, item)
            end
        end
  
        -- Replace original content with grouped content
        el.content = grouped
        return el
    end
  end