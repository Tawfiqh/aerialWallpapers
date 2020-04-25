import React from "react"
import JSONData from "../../content/output_parsed_file_list.json"

const JSONbuildtime = () => (
  <div style={{ maxWidth: `960px`, margin: `1.45rem` }}>
    <h1>{JSONData[0].id}</h1>
    <h1>Hello!</h1>
    <ul>
      {JSONData.map((data, index) => {
        return <li key={`content_item_${index}`}>{data.id}</li>
      })}
    </ul>
  </div>
)
export default JSONbuildtime
