# fms_life
Ось код для візуалізації скінченного автомата в https://dreampuf.github.io/GraphvizOnline/

digraph {
    rankdir="LR"
    
    sleeping [shape="circle" style="filled" fillcolor="yellow"]
    eating [shape="circle" style="filled" fillcolor=""]
    studying [shape="circle" style="filled" fillcolor=""]
    waking_up [shape="circle" style="filled" fillcolor=""]
    alarm [shape="circle" style="filled" fillcolor="red"]
    relax [shape="circle" style="filled" fillcolor="green"]
    // sports [shape="circle" style="filled" fillcolor=""]
    
    
    _ -> sleeping [fillcolor="#a6cee3" color="#1f78b4"]
    sleeping -> waking_up [fillcolor="#a6cee3" color=""]
    sleeping -> sleeping [fillcolor="#a6cee3" color=""]
    sleeping -> alarm [fillcolor="#a6cee3" color=""]
    alarm -> waking_up [fillcolor="#a6cee3" color=""]
    alarm -> sleeping [fillcolor="#a6cee3" color=""]
    waking_up -> eating [fillcolor="#a6cee3" color="#1f78b4"]
    waking_up -> sleeping [fillcolor="#a6cee3" color="#1f78b4"]
    waking_up -> studying [fillcolor="#a6cee3" color="#1f78b4"]
    eating -> studying [fillcolor="#a6cee3" color="#1f78b4"]
    eating -> eating [fillcolor="#a6cee3" color="#1f78b4"]
    studying -> studying [fillcolor="#a6cee3" color="#1f78b4"]
    studying -> eating [fillcolor="#a6cee3" color="#1f78b4"]
    studying -> relax [fillcolor="#a6cee3" color="#1f78b4"]
    studying -> sleeping [fillcolor="#a6cee3" color="#1f78b4"]
    relax -> studying [fillcolor="#a6cee3" color="#1f78b4"]
    relax -> sleeping [fillcolor="#a6cee3" color="#1f78b4"]
}

Також я прикріпив скріншот схеми у файлі 'screen.png'