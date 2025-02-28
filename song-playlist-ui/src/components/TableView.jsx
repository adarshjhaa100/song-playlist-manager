import React, { useEffect, useState } from "react";
import "./TableStyles.css";
import { getSong } from "../utils/requests";

const TableView = ({ data, columns }) => {
    console.log(data);
  const [sortedData, setSortedData] = useState(data);
  const [currentPage, setCurrentPage] = useState(1);
  const [rowsPerPage] = useState(10);
  const [sortConfig, setSortConfig] = useState({ key: null, direction: "asc" });
  const [searchStr, setSearchStr] = useState('');

  const handleSort = (column) => {
    const columnKey = column.key;
    let direction = "asc";
    if (sortConfig.key === columnKey && sortConfig.direction === "asc") {
      direction = "desc";
    }
    
    console.log(columnKey);
    let sorted = [];
    if(columnKey.type === "numberd"){
        sorted = [...sortedData].sort((a, b) => {
            if (Number.parseFloat(a[columnKey]) < Number.parseFloat(b[columnKey])) return direction === "asc" ? -1 : 1;
            if (Number.parseFloat(a[columnKey]) > Number.parseFloat(b[columnKey])) return direction === "asc" ? 1 : -1;
            return 0;
          });
    } else {
        sorted = [...sortedData].sort((a, b) => {
            if (a[columnKey] < b[columnKey]) return direction === "asc" ? -1 : 1;
            if (a[columnKey] > b[columnKey]) return direction === "asc" ? 1 : -1;
            return 0;
          });
    }
    setSortConfig({ key: columnKey, direction });
    setSortedData(sorted);
  };

  const indexOfLastRow = currentPage * rowsPerPage;
  const indexOfFirstRow = indexOfLastRow - rowsPerPage;
  const currentRows = sortedData.slice(indexOfFirstRow, indexOfLastRow);
  const totalPages = Math.ceil(sortedData.length / rowsPerPage);

  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  useEffect(()=>{
    setSortedData(data)
  },[data!=null?data.length:0]);

  return (
    <div className="table-container">
    <div className="search-bar">
        <input
        className="search-input"
        type="text"
        placeholder="Search by Title..."
        value={searchStr}
        onChange={(e) => setSearchStr(e.target.value)}
        />
    <button className="search-button" onClick={async ()=>{
        if(searchStr.trim() === '') setSortedData(data);
        else {
            const song = await getSong(searchStr);
            console.log("Song:", song);
            setSortedData([song]);
        }
    }}>
        Find
    </button>

    </div>
      <table className="styled-table">
        <thead>
          <tr>
            {columns.map((column) => (
              <th
                key={column.key}
                onClick={() => handleSort(column)}
                className="sortable-header"
              >
                {column.label}{" "}
                {sortConfig.key === column.key
                  ? sortConfig.direction === "asc"
                    ? "↑"
                    : "↓"
                  : ""}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {currentRows.map((row, index) => (
            <tr key={index}>
              {columns.map((column) => {
                return (<td key={column.key}>{row[column.key]}</td>)
              }
                
              )}
            </tr>
          ))}
        </tbody>
      </table>

          {/* Pagination Tab */}
      <div className="pagination">
        <button
          onClick={() => handlePageChange(1)}
          disabled={currentPage === 1}
        >
          First
        </button>
        <button
          onClick={() => handlePageChange(currentPage - 1)}
          disabled={currentPage === 1}
        >
          Previous
        </button>
        <span>
          Page {currentPage} of {totalPages}
        </span>
        <button
          onClick={() => handlePageChange(currentPage + 1)}
          disabled={currentPage === totalPages}
        >
          Next
        </button>
        <button
          onClick={() => handlePageChange(totalPages)}
          disabled={currentPage === totalPages}
        >
          Last
        </button>
      </div>
    </div>
  );
};

export default TableView;